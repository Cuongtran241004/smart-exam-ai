#!/usr/bin/env python3
"""
Simple test script for the Intelligent Online Exam Proctoring System API
"""

import requests
import json
import base64
import cv2
import numpy as np

def test_health():
    """Test health endpoint"""
    try:
        response = requests.get("http://localhost:8000/health")
        print("Health Check:")
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.json()}")
        return response.status_code == 200
    except Exception as e:
        print(f"Health check failed: {e}")
        return False

def test_root():
    """Test root endpoint"""
    try:
        response = requests.get("http://localhost:8000/")
        print("\nRoot Endpoint:")
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.json()}")
        return response.status_code == 200
    except Exception as e:
        print(f"Root endpoint failed: {e}")
        return False

def test_students():
    """Test students endpoint"""
    try:
        response = requests.get("http://localhost:8000/students")
        print("\nStudents Endpoint:")
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.json()}")
        return response.status_code == 200
    except Exception as e:
        print(f"Students endpoint failed: {e}")
        return False

def create_test_image():
    """Create a simple test image"""
    # Create a simple image with a face-like shape
    img = np.zeros((300, 300, 3), dtype=np.uint8)
    
    # Draw a simple face
    cv2.circle(img, (150, 150), 80, (255, 255, 255), -1)  # Face
    cv2.circle(img, (130, 130), 10, (0, 0, 0), -1)        # Left eye
    cv2.circle(img, (170, 130), 10, (0, 0, 0), -1)        # Right eye
    cv2.ellipse(img, (150, 170), (20, 10), 0, 0, 180, (0, 0, 0), 2)  # Mouth
    
    return img

def test_analyze_frame():
    """Test analyze_frame endpoint"""
    try:
        # Create test image
        img = create_test_image()
        
        # Convert to bytes
        _, buffer = cv2.imencode('.jpg', img)
        img_bytes = buffer.tobytes()
        
        # Test file upload
        files = {'file': ('test.jpg', img_bytes, 'image/jpeg')}
        response = requests.post("http://localhost:8000/analyze_frame", files=files)
        
        print("\nAnalyze Frame (File Upload):")
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.json()}")
        
        # Test base64
        img_base64 = base64.b64encode(img_bytes).decode('utf-8')
        data = {"image": img_base64}
        response = requests.post("http://localhost:8000/analyze_frame_base64", json=data)
        
        print("\nAnalyze Frame (Base64):")
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.json()}")
        
        return True
    except Exception as e:
        print(f"Analyze frame test failed: {e}")
        return False

def main():
    """Run all tests"""
    print("Testing Intelligent Online Exam Proctoring System API")
    print("=" * 60)
    
    tests = [
        ("Health Check", test_health),
        ("Root Endpoint", test_root),
        ("Students Endpoint", test_students),
        ("Analyze Frame", test_analyze_frame),
    ]
    
    results = []
    for test_name, test_func in tests:
        print(f"\n{'='*20} {test_name} {'='*20}")
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print(f"Test {test_name} failed with exception: {e}")
            results.append((test_name, False))
    
    print("\n" + "=" * 60)
    print("TEST RESULTS SUMMARY")
    print("=" * 60)
    
    passed = 0
    total = len(results)
    
    for test_name, result in results:
        status = "PASS" if result else "FAIL"
        print(f"{test_name}: {status}")
        if result:
            passed += 1
    
    print(f"\nOverall: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed!")
    else:
        print("❌ Some tests failed")

if __name__ == "__main__":
    main() 