# 🐾 Hệ Thống Phân Loại Giống Chó & Mèo

Ứng dụng web dùng AI để phân loại và nhận diện giống của chó và mèo từ hình ảnh.

## 📋 Yêu Cầu

- Python 3.8 trở lên
- pip (Package manager của Python)

## 🚀 Hướng Dẫn Cài Đặt

### 1. Clone hoặc tải về dự án

Đảm bảo bạn có tất cả các file sau trong cùng một thư mục:
- `app.py`
- `pet_breed_model_final.h5`
- `README.md`

### 2. Tạo môi trường ảo (Virtual Environment) - Khuyên dùng

#### Trên Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

#### Trên macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Cài Đặt Các Thư Viện Cần Thiết

```bash
pip install streamlit tensorflow numpy pillow
```

Hoặc cài từng package một:
```bash
pip install streamlit
pip install tensorflow
pip install numpy
pip install pillow
```

## ▶️ Chạy Chương Trình

### Bước 1: Mở Terminal/Command Prompt

Điều hướng đến thư mục chứa `app.py`:
```bash
cd /path/to/your/project
```

### Bước 2: Chạy ứng dụng Streamlit

```bash
streamlit run app.py
```

### Bước 3: Truy Cập Ứng Dụng

Ứng dụng sẽ tự động mở trong trình duyệt tại địa chỉ:
```
http://localhost:8501
```

Nếu không mở được, hãy sao chép đường dẫn trên vào trình duyệt của bạn.

## 💡 Cách Sử Dụng

1. **Tải lên ảnh**: Click nút "Upload một ảnh chó/mèo" để chọn ảnh từ máy tính
2. **Hoặc chụp ảnh**: Nếu máy có camera, bạn có thể chụp ảnh trực tiếp
3. **Xem kết quả**: Ứng dụng sẽ hiển thị giống chó/mèo được nhận diện

## 🔍 Các Giống Được Hỗ Trợ

### Chó:
- Chihuahua
- American Bulldog
- Beagle
- Shiba Inu
- Pug

### Mèo:
- Persian
- Maine Coon
- Bengal
- Siamese
- British Shorthair

## 📁 Cấu Trúc Thư Mục

```
├── app.py                      # File ứng dụng chính
├── pet_breed_model_final.h5   # Mô hình AI đã huấn luyện
└── README.md                   # File hướng dẫn này
```

## 🛠️ Khắc Phục Sự Cố

### Lỗi: "ModuleNotFoundError"
**Nguyên nhân**: Chưa cài đặt các thư viện cần thiết  
**Giải pháp**: Chạy lại câu lệnh cài đặt:
```bash
pip install streamlit tensorflow numpy pillow
```

### Lỗi: "Không tìm thấy model"
**Nguyên nhân**: File `pet_breed_model_final.h5` không ở cùng thư mục với `app.py`  
**Giải pháp**: Chuyển file model vào cùng thư mục với `app.py`

### Ứng dụng chạy chậm
**Giải pháp**: Đây là hành vi bình thường của lần chạy đầu tiên vì tensorflow cần khởi tạo

## 📝 Lưu Ý

- Ứng dụng yêu cầu kết nối internet để tải TensorFlow lần đầu
- Mô hình được tối ưu hóa cho ảnh chất lượng tốt (kích thước 224x224 pixels)
- Kết quả tốt nhất khi ảnh chứa rõ ràng mặt hoặc toàn bộ cơ thể của vật nuôi

## 📧 Hỗ Trợ

Nếu gặp bất kỳ vấn đề nào, hãy kiểm tra:
1. Python phiên bản 3.8+
2. Tất cả các thư viện đã được cài đặt
3. File model tồn tại trong thư mục dự án
4. Kết nối internet cho lần chạy đầu tiên

---
**Tạo ngày**: 2026-03-18  
**Phiên bản**: 1.0
