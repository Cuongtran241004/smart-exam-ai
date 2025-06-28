# 🎓 Intelligent Online Exam Proctoring System - FastAPI

Hệ thống giám sát thi trực tuyến thông minh được chuyển đổi thành API FastAPI với khả năng deploy lên Hugging Face Spaces.

## 🚀 Tính năng

- **Nhận diện khuôn mặt**: Xác minh danh tính thí sinh
- **Phát hiện đối tượng**: Phát hiện các vật dụng bị cấm (laptop, điện thoại, sách, TV)
- **Đếm người**: Đảm bảo chỉ có 1 người trong khung hình
- **Phát hiện gian lận**: Giám sát hành vi bất thường
- **API RESTful**: Dễ dàng tích hợp với các ứng dụng khác
- **Docker Support**: Containerized để dễ deploy
- **Hugging Face Ready**: Sẵn sàng deploy lên Hugging Face Spaces

## 📁 Cấu trúc dự án

```
.
├── app.py                 # FastAPI application chính
├── requirements.txt       # Python dependencies
├── Dockerfile            # Docker configuration
├── docker-compose.yml    # Docker Compose configuration
├── test_api.py           # Python test script
├── test_ui.html          # Web UI để test API
├── build_and_test.sh     # Script build và test
├── .huggingface/         # Hugging Face configuration
│   └── config.yaml
├── .github/workflows/    # GitHub Actions
│   └── deploy.yml
├── Code/                 # Original code directory
│   ├── models/          # AI models
│   ├── student_db/      # Student face database
│   └── *.py            # Core modules
└── README_FASTAPI.md    # This file
```

## 🛠️ Cài đặt và chạy

### Phương pháp 1: Sử dụng Docker (Khuyến nghị)

```bash
# Clone repository
git clone <your-repo-url>
cd Intelligent-Online-Exam-Proctoring-System

# Chạy script build và test tự động
chmod +x build_and_test.sh
./build_and_test.sh
```

Hoặc thủ công:

```bash
# Build và chạy với Docker Compose
docker-compose up --build

# Hoặc chạy Docker container trực tiếp
docker build -t proctoring-api .
docker run -p 8000:8000 proctoring-api
```

### Phương pháp 2: Cài đặt thủ công

```bash
# Cài đặt dependencies
pip install -r requirements.txt

# Chạy ứng dụng
uvicorn app:app --host 0.0.0.0 --port 8000
```

## 📚 API Documentation

Sau khi chạy ứng dụng, truy cập:

- **API Docs**: http://localhost:8000/docs
- **Health Check**: http://localhost:8000/health

### Các endpoints chính:

1. **GET /health** - Kiểm tra trạng thái API
2. **GET /students** - Lấy danh sách sinh viên
3. **POST /analyze_frame** - Phân tích frame từ file upload
4. **POST /analyze_frame_base64** - Phân tích frame từ base64

## 🧪 Testing

### Test với Python

```bash
python test_api.py
```

### Test với Web UI

Mở file `test_ui.html` trong browser để test API với giao diện web.

### Test với curl

```bash
# Health check
curl http://localhost:8000/health

# Get students
curl http://localhost:8000/students

# Analyze image file
curl -X POST -F "file=@test_image.jpg" http://localhost:8000/analyze_frame
```

## 🚀 Deploy lên Hugging Face Spaces

### Bước 1: Chuẩn bị

1. Tạo tài khoản trên [Hugging Face](https://huggingface.co/)
2. Tạo Space mới với type "Docker"
3. Lấy Hugging Face token

### Bước 2: Cấu hình

1. Thêm Hugging Face token vào GitHub Secrets:

   - Vào GitHub repository → Settings → Secrets and variables → Actions
   - Tạo secret `HUGGINGFACE_TOKEN` với token từ Hugging Face

2. Push code lên GitHub:

```bash
git add .
git commit -m "Add FastAPI support and Hugging Face deployment"
git push origin main
```

### Bước 3: Deploy

GitHub Actions sẽ tự động deploy lên Hugging Face Spaces khi push code lên branch main.

## 🔧 Cấu hình

### Environment Variables

Có thể cấu hình các biến môi trường:

```bash
# Trong docker-compose.yml
environment:
  - PYTHONPATH=/app
  - LOG_LEVEL=INFO
```

### Model Configuration

Đảm bảo các file model được đặt đúng vị trí:

- `Code/models/Headpose_customARC_ZoomShiftNoise.hdf5`
- `Code/models/shape_predictor_68_face_landmarks.dat`
- `Code/student_db/` - chứa ảnh sinh viên

## 🐛 Troubleshooting

### Lỗi thường gặp

1. **Model không load được**

   ```bash
   # Kiểm tra đường dẫn model
   ls -la Code/models/
   ```

2. **Face recognition không hoạt động**

   ```bash
   # Kiểm tra database sinh viên
   ls -la Code/student_db/
   ```

3. **Memory issues**
   ```bash
   # Tăng memory cho Docker
   docker run -m 4g -p 8000:8000 proctoring-api
   ```

### Logs

```bash
# Xem logs Docker
docker-compose logs -f

# Xem logs container
docker logs <container_id>
```

## 📊 Performance

- **Response Time**: ~1-3 giây cho mỗi frame
- **Memory Usage**: ~2-4GB RAM
- **CPU Usage**: ~50-80% CPU (tùy thuộc vào model)

## 🤝 Đóng góp

1. Fork repository
2. Tạo feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Tạo Pull Request

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

## 📞 Liên hệ

- **Email**: [your-email@example.com]
- **GitHub**: [your-github-username]
- **Project Link**: [https://github.com/your-username/your-repo-name]

## 🙏 Acknowledgments

- Original project by Apar Garg and Gopan Ravikumar Girija
- FastAPI framework
- Hugging Face Spaces for deployment
- OpenCV and TensorFlow for computer vision
