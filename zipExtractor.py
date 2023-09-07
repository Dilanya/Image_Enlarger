import zipfile
import os
from shutil import copy2

def extract_zip(path):
    code_dir = os.path.dirname(os.path.abspath(__file__))
    
    extraction_dir = os.path.join(code_dir, "extracted_files")
    os.makedirs(extraction_dir, exist_ok=True)

    with zipfile.ZipFile(path,"r") as zip_ref:
        zip_ref.extractall(extraction_dir)
        print("Extracted")

def main():
    path=input("Enter the path of the file: ")
    extract_zip(path)
if __name__=="__main__":
    main()



