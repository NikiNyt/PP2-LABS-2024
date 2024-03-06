import os

def pathex(path):
    if os.path.exists(path):
        print("Directory:", os.path.dirname(path))
        print("Filename:", os.path.basename(path))
    else:
        print("File does not exist")
        
        
path = r'C:\Users\nikita k\work\LAB6\PYTHON_Directories\test1.txt'
pathex(path)