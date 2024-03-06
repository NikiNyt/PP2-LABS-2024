import os
def isok(filename):
    print("File exists:", os.access(filename, os.F_OK))
    print("You can read this file:", os.access(filename, os.R_OK))
    print("You can write in this file:", os.access(filename, os.W_OK))
    print("You can execute this file:", os.access(filename, os.X_OK))
        
os.chdir("PYTHON_Directories")

filename = str(input())

isok(filename)
