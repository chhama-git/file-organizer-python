import os
import shutil

folder_path = "C:/Users/KRISHAN HUDDA/Downloads"

files = os.listdir(folder_path)

images_folder = os.path.join(folder_path, "Images")
pdf_folder = os.path.join(folder_path, "PDFs")

if not os.path.exists(images_folder):
    os.mkdir(images_folder)

if not os.path.exists(pdf_folder):
    os.mkdir(pdf_folder)

for file in files:
    file_path = os.path.join(folder_path, file)

    if os.path.isdir(file_path):
        continue

    if file.endswith(".jpg") or file.endswith(".png"):
        shutil.move(file_path, os.path.join(images_folder, file))

    elif file.endswith(".pdf"):
        shutil.move(file_path, os.path.join(pdf_folder, file))

print("Files organized successfully!")