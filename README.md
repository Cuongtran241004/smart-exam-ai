---
title: Intelligent Online Exam Proctoring System
emoji: 🎓
colorFrom: blue
colorTo: purple
sdk: docker
sdk_version: "latest"
app_file: app.py
pinned: false
---

# 🎓 Intelligent Online Exam Proctoring System

Hệ thống giám sát thi trực tuyến thông minh với nhận diện khuôn mặt và giám sát hành vi.

## 🚀 Tính năng

- **Nhận diện khuôn mặt**: Xác minh danh tính thí sinh
- **Phát hiện đối tượng**: Phát hiện các vật dụng bị cấm (laptop, điện thoại, sách, TV)
- **Đếm người**: Đảm bảo chỉ có 1 người trong khung hình
- **Phát hiện gian lận**: Giám sát hành vi bất thường
- **API RESTful**: Dễ dàng tích hợp với các ứng dụng khác

## 📚 API Endpoints

### Health Check

```
GET /health
```

### Phân tích frame

```
POST /analyze_frame
```

### Phân tích frame từ base64

```
POST /analyze_frame_base64
```

### Danh sách sinh viên

```
GET /students
```

## 🧪 Sử dụng API

### Python Example:

```python
import requests

# Health check
response = requests.get('https://cuongse-proctoring-system.hf.space/health')
print(response.json())

# Analyze image
with open('test_image.jpg', 'rb') as f:
    files = {'file': f}
    response = requests.post('https://cuongse-proctoring-system.hf.space/analyze_frame', files=files)
    print(response.json())
```

### JavaScript Example:

```javascript
// Health check
fetch("https://cuongse-proctoring-system.hf.space/health")
  .then((response) => response.json())
  .then((data) => console.log(data));
```

## 📖 API Documentation

Truy cập: https://cuongse-proctoring-system.hf.space/docs

## 🔧 Cấu hình

Để sử dụng đầy đủ tính năng, bạn cần:

1. **Models**: Upload các file model vào thư mục `Code/models/`
2. **Student Database**: Upload ảnh sinh viên vào thư mục `Code/student_db/`

## 📞 Hỗ trợ

Nếu gặp vấn đề, vui lòng kiểm tra:

- API Documentation: `/docs`
- Health Check: `/health`
- GitHub Repository: https://github.com/Cuongtran241004/smart-exam-ai

## 🙏 Acknowledgments

- Original project by Apar Garg and Gopan Ravikumar Girija
- FastAPI framework
- Hugging Face Spaces for deployment
- OpenCV and TensorFlow for computer vision

# OVERVIEW 📚

In this project, we have built an automatic online exam
proctoring system that provides improved authentication and
abnormal behavior monitoring of examinees in the online examination based on image information. We have used image processing and deep learning to build the system.

Refer to the [Report](https://github.com/AparGarg99/Intelligent-Online-Exam-Proctoring-System/blob/master/Documentation/ITSS_Project_Report.pdf) for more details.

---

# SYSTEM DEMO 🎥

![](https://github.com/AparGarg99/Intelligent-Online-Exam-Proctoring-System/blob/master/Miscellaneous/Dataset/demo.gif)

Watch the [Video](https://youtu.be/lGGHgPYJ4ig) for more details.

---

# INSTALLATION AND USER GUIDE 🔌

Refer to the [Installation Guide](https://github.com/AparGarg99/Intelligent-Online-Exam-Proctoring-System/blob/master/Documentation/Installation_Guide.pdf).

---

# AUTHORS 👨‍💻

|       Full Name        |       Email ID       |
| :--------------------: | :------------------: |
|       Apar Garg        | apargarg99@gmail.com |
| Gopan Ravikumar Girija | rggopan123@gmail.com |

---

# NEW FUNCTIONALITIES 🐣

- Instead of maintaining a database of student face images, face verification can be performed directly with the photo in the ID Card issued to the student. [Reference](https://github.com/mesutpiskin/id-card-detector)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![](https://github.com/AparGarg99/Intelligent-Online-Exam-Proctoring-System/blob/master/New_Functionalities/id_card_detection/demo_2.gif)

- Distance estimation b/w webcam and candidate to check if candidate is sitting at a reasonable distance from the webcam. [Reference](https://www.youtube.com/watch?v=jsoe1M2AjFk&t=2309s)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![](https://github.com/AparGarg99/Intelligent-Online-Exam-Proctoring-System/blob/master/New_Functionalities/distance_estimation/demo.gif)

---

# FUTURE WORK

- Lip reading
- Accurate eye tracking/gaze estimation.
- Accurate face spoofing detection.
- Detect nano-sized, non-wired devices such as Bluetooth earpieces,Spy eyewear, invisible smartwatch.
- Speaker verification [Ref1](https://github.com/Atul-Anand-Jha/Speaker-Identification-Python) | [Ref2](https://github.com/resemble-ai/Resemblyzer)

---

**_Don't forget to give a ⭐ if you like this project !!_**
