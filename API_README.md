# Intelligent Online Exam Proctoring System API

API FastAPI cho hệ thống giám sát thi trực tuyến thông minh với nhận diện khuôn mặt và giám sát hành vi.

## Tính năng

- **Nhận diện khuôn mặt**: Xác minh danh tính thí sinh
- **Phát hiện đối tượng**: Phát hiện các vật dụng bị cấm (laptop, điện thoại, sách, TV)
- **Đếm người**: Đảm bảo chỉ có 1 người trong khung hình
- **Phát hiện gian lận**: Giám sát hành vi bất thường
- **API RESTful**: Dễ dàng tích hợp với các ứng dụng khác

## Cài đặt

### Sử dụng Docker (Khuyến nghị)

```bash
# Build và chạy với Docker Compose
docker-compose up --build

# Hoặc chạy Docker container trực tiếp
docker build -t proctoring-api .
docker run -p 8000:8000 proctoring-api
```

### Cài đặt thủ công

```bash
# Cài đặt dependencies
pip install -r requirements.txt

# Chạy ứng dụng
uvicorn app:app --host 0.0.0.0 --port 8000
```

## API Endpoints

### 1. Health Check

```
GET /health
```

Kiểm tra trạng thái API và các model đã được load.

### 2. Phân tích frame

```
POST /analyze_frame
```

Phân tích một frame từ file ảnh upload.

**Request:**

- Content-Type: multipart/form-data
- Body: file ảnh

**Response:**

```json
{
  "people_count": 1,
  "banned_objects": [],
  "face_detected": true,
  "face_verified": true,
  "person_name": "student_name",
  "headpose_alert": false,
  "spoofing_alert": false,
  "alerts": []
}
```

### 3. Phân tích frame từ base64

```
POST /analyze_frame_base64
```

Phân tích một frame từ ảnh được encode base64.

**Request:**

```json
{
  "image": "base64_encoded_image_string"
}
```

### 4. Danh sách sinh viên

```
GET /students
```

Lấy danh sách sinh viên đã đăng ký.

## Sử dụng với Python

```python
import requests
import base64

# Upload file ảnh
with open('frame.jpg', 'rb') as f:
    files = {'file': f}
    response = requests.post('http://localhost:8000/analyze_frame', files=files)
    result = response.json()
    print(result)

# Sử dụng base64
with open('frame.jpg', 'rb') as f:
    image_data = base64.b64encode(f.read()).decode('utf-8')
    response = requests.post('http://localhost:8000/analyze_frame_base64',
                           json={'image': image_data})
    result = response.json()
    print(result)
```

## Sử dụng với JavaScript

```javascript
// Upload file
const formData = new FormData();
formData.append("file", fileInput.files[0]);

fetch("http://localhost:8000/analyze_frame", {
  method: "POST",
  body: formData,
})
  .then((response) => response.json())
  .then((data) => console.log(data));

// Sử dụng base64
const canvas = document.createElement("canvas");
const ctx = canvas.getContext("2d");
canvas.width = video.videoWidth;
canvas.height = video.videoHeight;
ctx.drawImage(video, 0, 0);
const base64Image = canvas.toDataURL("image/jpeg").split(",")[1];

fetch("http://localhost:8000/analyze_frame_base64", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
  },
  body: JSON.stringify({ image: base64Image }),
})
  .then((response) => response.json())
  .then((data) => console.log(data));
```

## Cấu trúc thư mục

```
.
├── app.py                 # FastAPI application
├── requirements.txt       # Python dependencies
├── Dockerfile            # Docker configuration
├── docker-compose.yml    # Docker Compose configuration
├── Code/                 # Original code directory
│   ├── models/          # AI models
│   ├── student_db/      # Student face database
│   └── *.py            # Core modules
└── API_README.md        # This file
```

## Deploy lên Hugging Face Spaces

1. Tạo repository trên Hugging Face Spaces
2. Push code lên repository
3. Hugging Face sẽ tự động build và deploy

### Cấu hình Hugging Face Spaces

Tạo file `.github/workflows/deploy.yml`:

```yaml
name: Deploy to Hugging Face Spaces

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Deploy to Spaces
        uses: huggingface/huggingface_hub@main
        with:
          repo-type: space
          space-sdk: docker
          space-config-path: .huggingface/config.yaml
```

## Troubleshooting

### Lỗi thường gặp

1. **Model không load được**: Kiểm tra đường dẫn đến các file model trong thư mục `Code/models/`
2. **Face recognition không hoạt động**: Đảm bảo có ảnh sinh viên trong thư mục `Code/student_db/`
3. **Memory issues**: Giảm kích thước frame hoặc tăng memory cho container

### Logs

```bash
# Xem logs Docker
docker-compose logs -f

# Xem logs container
docker logs <container_id>
```

## Đóng góp

1. Fork repository
2. Tạo feature branch
3. Commit changes
4. Push to branch
5. Tạo Pull Request

## License

MIT License
