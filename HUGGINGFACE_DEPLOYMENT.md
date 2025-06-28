# 🚀 Hướng dẫn Deploy lên Hugging Face Spaces

## 📋 Checklist trước khi deploy

### ✅ Đã hoàn thành:

- [x] Code đã được push lên GitHub
- [x] GitHub Actions workflow đã được cấu hình và sửa lỗi
- [x] Hugging Face config file đã được tạo

### 🔄 Cần thực hiện:

## Bước 1: Tạo Hugging Face Space

1. **Truy cập Hugging Face**:

   - Vào https://huggingface.co/
   - Đăng nhập hoặc tạo tài khoản

2. **Tạo Space mới**:
   - Click "New Space" hoặc "Create Space"
   - Chọn **"Docker"** làm SDK
   - Đặt tên: `your-username/proctoring-system` (thay `your-username` bằng username của bạn)
   - Chọn "Public" hoặc "Private"
   - Click "Create Space"

## Bước 2: Lấy Hugging Face Token

1. **Tạo Access Token**:
   - Vào https://huggingface.co/settings/tokens
   - Click "New token"
   - Đặt tên: "GitHub Actions"
   - Chọn quyền: **"Write"**
   - Copy token (dạng: `hf_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`)

## Bước 3: Cấu hình GitHub Secrets

1. **Vào GitHub repository**:

   - Truy cập: https://github.com/Cuongtran241004/smart-exam-ai
   - Vào tab "Settings"

2. **Thêm Secret**:
   - Vào "Secrets and variables" → "Actions"
   - Click "New repository secret"
   - **Name**: `HUGGINGFACE_TOKEN`
   - **Value**: Paste token từ bước 2
   - Click "Add secret"

## Bước 4: Kiểm tra GitHub Actions

1. **Vào tab Actions**:
   - Truy cập: https://github.com/Cuongtran241004/smart-exam-ai/actions
   - Kiểm tra workflow "Deploy to Hugging Face Spaces"
   - Nếu chưa chạy, click "Run workflow"

## Bước 5: Monitor Deploy Process

### GitHub Actions Logs:

- Vào tab Actions trên GitHub
- Click vào workflow đang chạy
- Xem logs để theo dõi quá trình build

### Hugging Face Space:

- Vào Space của bạn trên Hugging Face
- Kiểm tra trạng thái build
- Xem logs nếu có lỗi

## 🔧 Troubleshooting

### Lỗi thường gặp:

1. **Token không hợp lệ**:

   ```
   Error: Invalid token
   ```

   **Giải pháp**: Tạo lại token với quyền "Write"

2. **Space không tồn tại**:

   ```
   Error: Space not found
   ```

   **Giải pháp**: Tạo Space trước khi deploy

3. **Docker build failed**:

   ```
   Error: Docker build failed
   ```

   **Giải pháp**: Kiểm tra Dockerfile và requirements.txt

4. **Model files missing**:

   ```
   Error: Model not found
   ```

   **Giải pháp**: Đảm bảo các file model trong thư mục `Code/models/`

5. **GitHub Actions workflow error**:
   ```
   Error: Can't find 'action.yml'
   ```
   **Giải pháp**: ✅ Đã sửa - sử dụng huggingface-cli thay vì action

## 📊 Kiểm tra sau khi deploy

### 1. Health Check:

```bash
curl https://your-username-proctoring-system.hf.space/health
```

### 2. API Documentation:

- Truy cập: `https://your-username-proctoring-system.hf.space/docs`

### 3. Test Endpoints:

```bash
# Health check
curl https://your-username-proctoring-system.hf.space/health

# Get students
curl https://your-username-proctoring-system.hf.space/students
```

### 4. Sử dụng script kiểm tra:

```bash
python check_deployment.py
```

## 🔄 Update và Redeploy

Để update code và redeploy:

```bash
# Thay đổi code
git add .
git commit -m "Update code"
git push origin main
```

GitHub Actions sẽ tự động trigger deploy mới.

## 📱 Sử dụng API sau khi deploy

### Python Example:

```python
import requests

# Health check
response = requests.get('https://your-username-proctoring-system.hf.space/health')
print(response.json())

# Analyze image
with open('test_image.jpg', 'rb') as f:
    files = {'file': f}
    response = requests.post('https://your-username-proctoring-system.hf.space/analyze_frame', files=files)
    print(response.json())
```

### JavaScript Example:

```javascript
// Health check
fetch("https://your-username-proctoring-system.hf.space/health")
  .then((response) => response.json())
  .then((data) => console.log(data));
```

## 📞 Hỗ trợ

Nếu gặp vấn đề:

1. Kiểm tra GitHub Actions logs
2. Kiểm tra Hugging Face Space logs
3. Đảm bảo token có quyền "Write"
4. Kiểm tra tên Space đúng format
5. Sử dụng script `check_deployment.py` để kiểm tra

## 🎉 Thành công!

Sau khi deploy thành công, bạn sẽ có:

- ✅ API endpoint: `https://your-username-proctoring-system.hf.space`
- ✅ API docs: `https://your-username-proctoring-system.hf.space/docs`
- ✅ Health check: `https://your-username-proctoring-system.hf.space/health`

## 🔄 Workflow đã được sửa

GitHub Actions workflow đã được cập nhật để sử dụng `huggingface-cli` thay vì action không tồn tại. Workflow mới sẽ:

1. Setup Python environment
2. Install huggingface_hub
3. Create space nếu chưa tồn tại
4. Push code lên space
