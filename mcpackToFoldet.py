import os
import zipfile

# Nhập đường dẫn thư mục chứa các tệp .mcpack và .zip từ người dùng
path = input("Enter the directory path: ")

# Định nghĩa hàm để giải nén và xóa tệp .mcpack hoặc .zip
def extract_archive(archive):
    # Xác định loại tệp (mcpack hoặc zip) dựa trên đuôi (extension)
    file_extension = os.path.splitext(archive)[1].lower()

    if file_extension == '.mcpack' or file_extension == '.zip':
        # Giải nén tệp .mcpack hoặc .zip
        with zipfile.ZipFile(archive, 'r') as zip_ref:
            # Xác định thư mục đích cho việc giải nén
            target_folder = os.path.join(os.path.dirname(archive), os.path.splitext(os.path.basename(archive))[0])
            zip_ref.extractall(target_folder)

        # Xóa tệp .mcpack hoặc .zip sau khi giải nén
        os.remove(archive)

        # In thông báo về việc giải nén tệp lên console
        print(f"Extracted: {archive}")
    else:
        print(f"Skipped: {archive} (unsupported file type)")

try:
    # Lặp qua tất cả các tệp trong thư mục và các thư mục con
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith((".mcpack", ".zip")):
                archive_path = os.path.join(root, file)
                extract_archive(archive_path)  # Giải nén tệp .mcpack hoặc .zip

    # Thông báo khi xử lý hoàn thành
    print("Processing complete.")
except Exception as e:
    # Thông báo lỗi nếu có lỗi xảy ra
    print(f"An error occurred: {e}")
