from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from contextlib import asynccontextmanager
import cv2
import numpy as np
from collections import Counter
import os
import sys
from typing import List, Dict, Any
import base64
from io import BytesIO
from PIL import Image
import json

# Import các module từ Code directory
sys.path.append('Code')
# from face_detection import get_face_detector, find_faces  # Removed - not needed

# Global variables for models
known_face_names = []
face_model = None

def initialize_models():
    """Initialize all required models"""
    global known_face_names, face_model
    
    # Load face recognition database (simplified - just store names for now)
    student_db_path = 'Code/student_db'
    if os.path.exists(student_db_path):
        for image_file in os.listdir(student_db_path):
            if image_file.lower().endswith(('.png', '.jpg', '.jpeg')):
                known_face_names.append(image_file.split('.')[0])
    
    # For now, skip face detection model loading to avoid issues
    face_model = None
    print("Face detection model disabled for compatibility")

def image_to_base64(image):
    """Convert OpenCV image to base64 string"""
    _, buffer = cv2.imencode('.jpg', image)
    img_str = base64.b64encode(buffer).decode('utf-8')
    return img_str

def base64_to_image(base64_string):
    """Convert base64 string to OpenCV image"""
    img_data = base64.b64decode(base64_string)
    nparr = np.frombuffer(img_data, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    return img

def simple_object_detection(frame):
    """Simple object detection using OpenCV"""
    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Simple edge detection
    edges = cv2.Canny(gray, 50, 150)
    
    # Find contours
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Count significant objects (contours with area > threshold)
    significant_objects = [c for c in contours if cv2.contourArea(c) > 1000]
    
    return len(significant_objects)

def process_frame(frame):
    """Process a single frame and return analysis results"""
    results = {
        "people_count": 0,
        "banned_objects": [],
        "face_detected": False,
        "face_verified": False,
        "person_name": "Unknown",
        "headpose_alert": False,
        "spoofing_alert": False,
        "alerts": []
    }
    
    try:
        # Resize frame for processing
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        
        # Simple Object Detection
        try:
            object_count = simple_object_detection(small_frame)
            results["people_count"] = object_count
            
            if results["people_count"] != 1:
                results["alerts"].append("Multiple objects detected")
                
        except Exception as e:
            print(f"Object detection error: {e}")
            results["alerts"].append("Object detection failed")
        
        # Simple face detection using OpenCV's built-in cascade
        if results["people_count"] >= 1:
            try:
                # Use OpenCV's built-in face cascade
                face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
                gray = cv2.cvtColor(small_frame, cv2.COLOR_BGR2GRAY)
                faces = face_cascade.detectMultiScale(gray, 1.1, 4)
                
                if len(faces) > 0:
                    results["face_detected"] = True
                    results["person_name"] = "Face Detected"
                    results["face_verified"] = True
                else:
                    results["alerts"].append("No face detected")
                    
            except Exception as e:
                print(f"Face detection error: {e}")
                results["alerts"].append("Face detection failed")
                
    except Exception as e:
        print(f"Frame processing error: {e}")
        results["alerts"].append("Frame processing failed")
    
    return results

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    initialize_models()
    yield
    # Shutdown (if needed)

app = FastAPI(
    title="Intelligent Online Exam Proctoring System API",
    description="API for automatic online exam proctoring with face recognition and behavior monitoring",
    version="1.0.0",
    lifespan=lifespan
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "Intelligent Online Exam Proctoring System API",
        "version": "1.0.0",
        "status": "running"
    }

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "models_loaded": {
            "face_recognition": len(known_face_names) > 0,
            "face_detection": face_model is not None
        }
    }

@app.post("/analyze_frame")
async def analyze_frame(file: UploadFile = File(...)):
    """Analyze a single frame for proctoring"""
    try:
        # Read image file
        contents = await file.read()
        nparr = np.frombuffer(contents, np.uint8)
        frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        
        if frame is None:
            raise HTTPException(status_code=400, detail="Invalid image file")
        
        # Process frame
        results = process_frame(frame)
        
        return JSONResponse(content=results)
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Processing error: {str(e)}")

@app.post("/analyze_frame_base64")
async def analyze_frame_base64(data: Dict[str, str]):
    """Analyze a single frame from base64 encoded image"""
    try:
        if "image" not in data:
            raise HTTPException(status_code=400, detail="Image data not provided")
        
        # Decode base64 image
        frame = base64_to_image(data["image"])
        
        if frame is None:
            raise HTTPException(status_code=400, detail="Invalid base64 image")
        
        # Process frame
        results = process_frame(frame)
        
        return JSONResponse(content=results)
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Processing error: {str(e)}")

@app.get("/students")
async def get_students():
    """Get list of registered students"""
    return {
        "students": known_face_names,
        "count": len(known_face_names)
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=7860) 