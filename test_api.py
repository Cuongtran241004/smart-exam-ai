import requests
import base64
import json
from PIL import Image
import numpy as np
import cv2

def test_health():
    """Test health endpoint"""
    try:
        response = requests.get('http://localhost:8000/health')
        print("Health Check:", response.json())
        return response.status_code == 200
    except Exception as e:
        print(f"Health check failed: {e}")
        return False

def test_students():
    """Test students endpoint"""
    try:
        response = requests.get('http://localhost:8000/students')
        print("Students:", response.json())
        return response.status_code == 200
    except Exception as e:
        print(f"Students endpoint failed: {e}")
        return False

def create_test_image():
    """Create a simple test image"""
    # Create a simple test image
    img = np.zeros((480, 640, 3), dtype=np.uint8)
    img[:] = (128, 128, 128)  # Gray background
    
    # Add some text
    cv2.putText(img, "Test Image", (200, 240), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    
    return img

def test_analyze_frame():
    """Test analyze_frame endpoint"""
    try:
        # Create test image
        test_img = create_test_image()
        
        # Save to temporary file
        cv2.imwrite('test_frame.jpg', test_img)
        
        # Upload file
        with open('test_frame.jpg', 'rb') as f:
            files = {'file': f}
            response = requests.post('http://localhost:8000/analyze_frame', files=files)
        
        print("Analyze Frame:", response.json())
        return response.status_code == 200
    except Exception as e:
        print(f"Analyze frame failed: {e}")
        return False

def test_analyze_frame_base64():
    """Test analyze_frame_base64 endpoint"""
    try:
        # Create test image
        test_img = create_test_image()
        
        # Convert to base64
        _, buffer = cv2.imencode('.jpg', test_img)
        img_str = base64.b64encode(buffer).decode('utf-8')
        
        # Send request
        response = requests.post('http://localhost:8000/analyze_frame_base64', 
                               json={'image': img_str})
        
        print("Analyze Frame Base64:", response.json())
        return response.status_code == 200
    except Exception as e:
        print(f"Analyze frame base64 failed: {e}")
        return False

def main():
    """Run all tests"""
    print("Testing Intelligent Online Exam Proctoring System API")
    print("=" * 50)
    
    tests = [
        ("Health Check", test_health),
        ("Students", test_students),
        ("Analyze Frame", test_analyze_frame),
        ("Analyze Frame Base64", test_analyze_frame_base64)
    ]
    
    results = []
    for test_name, test_func in tests:
        print(f"\nRunning {test_name}...")
        try:
            result = test_func()
            results.append((test_name, result))
            print(f"{test_name}: {'PASS' if result else 'FAIL'}")
        except Exception as e:
            print(f"{test_name}: ERROR - {e}")
            results.append((test_name, False))
    
    print("\n" + "=" * 50)
    print("Test Results Summary:")
    for test_name, result in results:
        status = "PASS" if result else "FAIL"
        print(f"{test_name}: {status}")
    
    # Clean up
    try:
        import os
        if os.path.exists('test_frame.jpg'):
            os.remove('test_frame.jpg')
    except:
        pass

if __name__ == "__main__":
    main() 