import os
import shutil

# Folder jahan se files organize karni hain
source_folder = "test_folder"

#  Extensions ke base pe folder types
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mkv"],
    "Others": []
}

def organize_files():
    for filename in os.listdir(source_folder):
        file_path = os.path.join(source_folder, filename)

        if os.path.isfile(file_path):
            file_ext = os.path.splitext(filename)[1].lower()
            moved = False

            for folder_name, extensions in file_types.items():
                if file_ext in extensions:
                    folder_path = os.path.join(source_folder, folder_name)
                    os.makedirs(folder_path, exist_ok=True)
                    shutil.move(file_path, os.path.join(folder_path, filename))
                    print(f"Moved: {filename} → {folder_name}")
                    moved = True
                    break

            if not moved:
                other_path = os.path.join(source_folder, "Others")
                os.makedirs(other_path, exist_ok=True)
                shutil.move(file_path, os.path.join(other_path, filename))
                print(f"Moved: {filename} → Others")

if __name__ == "__main__":
    organize_files()
