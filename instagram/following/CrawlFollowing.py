import requests
import os

# URL của trang Instagram bạn muốn truy cập
url = "https://www.instagram.com/sontungmtp/"

# Gửi yêu cầu GET đến trang Instagram
response = requests.get(url)

# Kiểm tra mã phản hồi từ server (200 là thành công)
if response.status_code == 200:
    print("Trang đã được tải thành công!")
    
    # Đảm bảo thư mục output tồn tại
    output_dir = './instagram/following/output'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Định nghĩa đường dẫn đến file sẽ lưu dữ liệu
    file_path = os.path.join(output_dir, 'ins.html')
    
    # Ghi nội dung HTML vào file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(response.text)
    
    print(f"Dữ liệu đã được ghi vào {file_path}")
else:
    print(f"Không thể truy cập trang, mã lỗi: {response.status_code}")
