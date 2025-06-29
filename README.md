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

## 🚀 Live Demo

**Hugging Face Space**: [https://huggingface.co/spaces/your-username/proctoring-system](https://huggingface.co/spaces/your-username/proctoring-system)

**API Endpoints**:

- Health Check: `https://your-username-proctoring-system.hf.space/health`
- API Documentation: `https://your-username-proctoring-system.hf.space/docs`
- Analyze Frame: `https://your-username-proctoring-system.hf.space/analyze_frame`

## 📋 Features

- **Face Detection & Recognition**: Automatic detection and verification of student faces
- **Behavior Monitoring**: Real-time monitoring of exam behavior
- **Object Detection**: Detection of banned objects and multiple people
- **Head Pose Analysis**: Monitoring head position and movement
- **Spoofing Detection**: Prevention of face spoofing attacks
- **RESTful API**: Easy integration with existing systems

## 🛠️ Technology Stack

- **Backend**: FastAPI (Python)
- **Computer Vision**: OpenCV, NumPy
- **Face Recognition**: Custom face detection models
- **Deployment**: Docker, Hugging Face Spaces
- **Port**: 7860 (optimized for Hugging Face deployment)

## 🚀 Quick Start

### Local Development

1. **Clone the repository**:

   ```bash
   git clone https://github.com/Cuongtran241004/smart-exam-ai.git
   cd smart-exam-ai
   ```

2. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:
   ```bash
   uvicorn app:app --host 0.0.0.0 --port 7860 --reload
   ```

### Docker Deployment

1. **Build the Docker image**:

   ```bash
   docker build -t proctoring-system .
   ```

2. **Run the container**:
   ```bash
   docker run -p 7860:7860 proctoring-system
   ```

### Hugging Face Deployment

The application is configured to run on **port 7860** for optimal Hugging Face Spaces deployment.

1. **Create a Hugging Face Space**:

   - Go to https://huggingface.co/spaces
   - Choose "Docker" as SDK
   - Set port to 7860

2. **Deploy using GitHub Actions**:
   - Push code to GitHub
   - GitHub Actions will automatically deploy to Hugging Face

## 📡 API Endpoints

### Health Check

```bash
GET /health
```

### Analyze Frame

```bash
POST /analyze_frame
Content-Type: multipart/form-data
```

**Request**: Upload image file
**Response**: JSON with analysis results

### Analyze Frame (Base64)

```bash
POST /analyze_frame_base64
Content-Type: application/json
```

**Request**:

```json
{
  "image": "base64_encoded_image_string"
}
```

## 🔧 Configuration

### Environment Variables

- `PORT`: Application port (default: 7860)
- `HOST`: Application host (default: 0.0.0.0)

### Model Configuration

- Face detection models: `Code/models/`
- Student database: `Code/student_db/`

## 📊 API Response Format

```json
{
  "people_count": 1,
  "banned_objects": [],
  "face_detected": true,
  "face_verified": true,
  "person_name": "Student Name",
  "headpose_alert": false,
  "spoofing_alert": false,
  "alerts": []
}
```

## 🧪 Testing

### Test API Endpoints

```bash
python test_api.py
```

### Test UI

Open `test_ui.html` in your browser to test the API interactively.

### Check Deployment

```bash
python check_deployment.py
```

## 📁 Project Structure

```
├── app.py                 # Main FastAPI application
├── Dockerfile            # Docker configuration
├── requirements.txt      # Python dependencies
├── Code/                 # Core modules
│   ├── models/          # AI models
│   ├── student_db/      # Student database
│   └── face_detection.py
├── .huggingface/        # Hugging Face configuration
│   └── config.yaml
├── test_api.py          # API testing script
├── test_ui.html         # Web UI for testing
└── README.md            # This file
```

## 🔄 Deployment Status

- ✅ Docker configuration optimized for port 7860
- ✅ Hugging Face Space configuration ready
- ✅ GitHub Actions workflow configured
- ✅ Health check endpoint available
- ✅ API documentation accessible

## 📞 Support

For issues and questions:

1. Check GitHub Actions logs
2. Review Hugging Face Space logs
3. Test with `check_deployment.py`
4. Open an issue on GitHub

## 📄 License

MIT License - see LICENSE file for details.

---

**Note**: This application is configured to run on port 7860 for optimal deployment on Hugging Face Spaces. The port configuration is set in both the Dockerfile and the application startup command.

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
