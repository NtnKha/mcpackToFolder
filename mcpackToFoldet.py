import os
import zipfile

def extract_archive(archive):
    """
    Extract an archive file and delete the original file.
    """
    file_extension = os.path.splitext(archive)[1].lower()

    if file_extension == '.mcpack' or file_extension == '.zip':
        with zipfile.ZipFile(archive, 'r') as zip_ref:
            target_folder = os.path.join(os.path.dirname(archive), os.path.splitext(os.path.basename(archive))[0])
            zip_ref.extractall(target_folder)

        os.remove(archive)
        print(f"Extracted: {archive}")
    else:
        print(f"Skipped: {archive} (unsupported file type)")

def process_directory(path):
    """
    Process all files in a directory and its subdirectories.
    """
    try:
        for root, dirs, files in os.walk(path):
            for file in files:
                if file.endswith(('.mcpack', '.zip')):
                    archive_path = os.path.join(root, file)
                    extract_archive(archive_path)

        print("Processing complete.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Get the directory path from the user
    path = input("Enter the directory path: ")

    # Process the directory
    process_directory(path)
