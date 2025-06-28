#!/usr/bin/env python3
"""
Script để kiểm tra trạng thái deploy trên Hugging Face Spaces
"""

import requests
import time
import sys
import json

def check_huggingface_space(username, space_name):
    """Kiểm tra trạng thái Hugging Face Space"""
    base_url = f"https://{username}-{space_name}.hf.space"
    
    print(f"🔍 Kiểm tra Space: {base_url}")
    print("=" * 50)
    
    # Test health endpoint
    try:
        print("1. Kiểm tra Health Endpoint...")
        response = requests.get(f"{base_url}/health", timeout=10)
        if response.status_code == 200:
            data = response.json()
            print("✅ Health Check: PASSED")
            print(f"   Status: {data.get('status', 'unknown')}")
            print(f"   Models loaded: {data.get('models_loaded', {})}")
        else:
            print(f"❌ Health Check: FAILED (Status: {response.status_code})")
    except Exception as e:
        print(f"❌ Health Check: ERROR - {e}")
    
    # Test students endpoint
    try:
        print("\n2. Kiểm tra Students Endpoint...")
        response = requests.get(f"{base_url}/students", timeout=10)
        if response.status_code == 200:
            data = response.json()
            print("✅ Students Endpoint: PASSED")
            print(f"   Students count: {data.get('count', 0)}")
            print(f"   Students: {data.get('students', [])}")
        else:
            print(f"❌ Students Endpoint: FAILED (Status: {response.status_code})")
    except Exception as e:
        print(f"❌ Students Endpoint: ERROR - {e}")
    
    # Test API docs
    try:
        print("\n3. Kiểm tra API Documentation...")
        response = requests.get(f"{base_url}/docs", timeout=10)
        if response.status_code == 200:
            print("✅ API Documentation: PASSED")
            print(f"   URL: {base_url}/docs")
        else:
            print(f"❌ API Documentation: FAILED (Status: {response.status_code})")
    except Exception as e:
        print(f"❌ API Documentation: ERROR - {e}")
    
    # Test root endpoint
    try:
        print("\n4. Kiểm tra Root Endpoint...")
        response = requests.get(base_url, timeout=10)
        if response.status_code == 200:
            data = response.json()
            print("✅ Root Endpoint: PASSED")
            print(f"   Message: {data.get('message', 'unknown')}")
            print(f"   Version: {data.get('version', 'unknown')}")
        else:
            print(f"❌ Root Endpoint: FAILED (Status: {response.status_code})")
    except Exception as e:
        print(f"❌ Root Endpoint: ERROR - {e}")

def main():
    print("🚀 Hugging Face Space Deployment Checker")
    print("=" * 50)
    
    # Lấy thông tin từ user
    username = input("Nhập Hugging Face username: ").strip()
    space_name = input("Nhập tên Space (mặc định: proctoring-system): ").strip()
    
    if not space_name:
        space_name = "proctoring-system"
    
    if not username:
        print("❌ Username không được để trống!")
        sys.exit(1)
    
    print(f"\n🎯 Kiểm tra Space: {username}/{space_name}")
    print("⏳ Đang kiểm tra...")
    
    # Kiểm tra space
    check_huggingface_space(username, space_name)
    
    print("\n" + "=" * 50)
    print("📋 Tóm tắt:")
    print(f"   Space URL: https://{username}-{space_name}.hf.space")
    print(f"   API Docs: https://{username}-{space_name}.hf.space/docs")
    print(f"   Health Check: https://{username}-{space_name}.hf.space/health")
    
    print("\n💡 Lưu ý:")
    print("   - Nếu tất cả test PASSED: Space đã deploy thành công!")
    print("   - Nếu có test FAILED: Kiểm tra GitHub Actions logs")
    print("   - Nếu có test ERROR: Space có thể chưa được tạo hoặc đang build")

if __name__ == "__main__":
    main() 