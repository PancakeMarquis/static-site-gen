import os
import shutil
import sys

from copystatic import copy_files_recursive
from generate_page import generate_page, generate_pages_recursive


dir_path_static = "./static"
dir_path_docs = "./docs"



def main():
    if len(sys.argv) > 1:
        base_path = sys.argv[1]
    else:
        base_path = "/"
    print("Deleting docs directory...")
    if os.path.exists(dir_path_docs):
        shutil.rmtree(dir_path_docs)

    print("Copying static files to docs directory...")
    copy_files_recursive(dir_path_static, dir_path_docs)
    
    print("Generating pages...")
    generate_pages_recursive("content/", "template.html", "docs/", base_path)



main()
