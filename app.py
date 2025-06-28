from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import cv2
import numpy as np
import face_recognition
import dlib
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
from object_detection import yoloV3Detect
from landmark_models import *
from face_spoofing import *
from headpose_estimation import *
from face_detection import get_face_detector, find_faces

app = FastAPI(
    title="Intelligent Online Exam Proctoring System API",
    description="API for automatic online exam proctoring with face recognition and behavior monitoring",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Global variables for models
known_face_encodings = []
known_face_names = []
h_model = None
face_model = None
predictor = None

def initialize_models():
    """Initialize all required models"""
    global known_face_encodings, known_face_names, h_model, face_model, predictor
    
    # Load face recognition database
    student_db_path = 'Code/student_db'
    if os.path.exists(student_db_path):
        for image_file in os.listdir(student_db_path):
            if image_file.lower().endswith(('.png', '.jpg', '.jpeg')):
                image_path = os.path.join(student_db_path, image_file)
                try:
                    obama_image = face_recognition.load_image_file(image_path)
                    obama_face_encoding = face_recognition.face_encodings(obama_image)[0]
                    known_face_encodings.append(obama_face_encoding)
                    known_face_names.append(image_file.split('.')[0])
                except Exception as e:
                    print(f"Error loading {image_file}: {e}")
    
    # Load headpose model
    try:
        h_model = load_hp_model('Code/models/Headpose_customARC_ZoomShiftNoise.hdf5')
    except Exception as e:
        print(f"Error loading headpose model: {e}")
    
    # Load face detection model
    try:
        face_model = get_face_detector()
    except Exception as e:
        print(f"Error loading face detection model: {e}")
    
    # Load face landmark model
    try:
        predictor = dlib.shape_predictor("Code/models/shape_predictor_68_face_landmarks.dat")
    except Exception as e:
        print(f"Error loading face landmark model: {e}")

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
        
        # Object Detection
        try:
            fboxes, fclasses = yoloV3Detect(small_frame)
            to_detect = ['person', 'laptop', 'cell phone', 'book', 'tv']
            
            temp1, temp2 = [], []
            for i in range(len(fclasses)):
                if fclasses[i] in to_detect:
                    temp1.append(fboxes[i])
                    temp2.append(fclasses[i])
            
            count_items = Counter(temp2)
            results["people_count"] = count_items.get('person', 0)
            
            banned_objects = []
            for obj in ['laptop', 'cell phone', 'book', 'tv']:
                if count_items.get(obj, 0) > 0:
                    banned_objects.append(obj)
            results["banned_objects"] = banned_objects
            
            if results["people_count"] != 1:
                results["alerts"].append("Multiple people detected")
            
            if banned_objects:
                results["alerts"].append(f"Banned objects detected: {', '.join(banned_objects)}")
                
        except Exception as e:
            print(f"Object detection error: {e}")
            results["alerts"].append("Object detection failed")
        
        # Face Detection and Recognition
        if results["people_count"] == 1:
            try:
                faces = find_faces(small_frame, face_model)
                if len(faces) > 0:
                    results["face_detected"] = True
                    
                    # Face Recognition
                    face_locations = [[faces[0][1], faces[0][2], faces[0][3], faces[0][0]]]
                    rgb_small_frame = small_frame[:, :, ::-1]
                    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
                    
                    if face_encodings:
                        face_encoding = face_encodings[0]
                        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                        
                        if len(face_distances) > 0:
                            best_match_index = np.argmin(face_distances)
                            if matches[best_match_index]:
                                results["person_name"] = known_face_names[best_match_index]
                                results["face_verified"] = True
                            else:
                                results["alerts"].append("Face not recognized")
                        else:
                            results["alerts"].append("No face encodings found")
                    else:
                        results["alerts"].append("No face encodings generated")
                else:
                    results["alerts"].append("No face detected")
                    
            except Exception as e:
                print(f"Face detection error: {e}")
                results["alerts"].append("Face detection failed")
        
        # Headpose Estimation
        if results["face_detected"] and h_model is not None:
            try:
                # Add headpose estimation logic here
                # This would use the h_model to detect head pose
                pass
            except Exception as e:
                print(f"Headpose estimation error: {e}")
        
        # Face Spoofing Detection
        if results["face_detected"]:
            try:
                # Add face spoofing detection logic here
                pass
            except Exception as e:
                print(f"Face spoofing detection error: {e}")
                
    except Exception as e:
        print(f"Frame processing error: {e}")
        results["alerts"].append("Frame processing failed")
    
    return results

@app.on_event("startup")
async def startup_event():
    """Initialize models on startup"""
    initialize_models()

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
            "face_recognition": len(known_face_encodings) > 0,
            "headpose_model": h_model is not None,
            "face_detection": face_model is not None,
            "face_landmarks": predictor is not None
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
    uvicorn.run(app, host="0.0.0.0", port=8000) 