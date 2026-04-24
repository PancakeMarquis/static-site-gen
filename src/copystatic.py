import os, shutil

def copy_files_recursive(src, dest):
    if not os.path.exists(dest):
        os.mkdir(dest)
    files = os.listdir(src)
    
    for item in files:
        file_path = os.path.join(src, item)
        dest_path = os.path.join(dest, item)
        print(f" * {file_path} -> {dest_path}")
        if os.path.isfile(file_path):
            shutil.copy(file_path, dest_path)
        else:
            copy_files_recursive(file_path, dest_path)