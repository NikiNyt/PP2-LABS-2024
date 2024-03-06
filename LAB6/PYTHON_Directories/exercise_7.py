import os

file1 = r"C:\Users\nikita k\work\LAB6\PYTHON_Directories\write_here.txt"
file2 = r"test1.txt"

os.chdir(r"C:\Users\nikita k\work\LAB6\PYTHON_Directories")

with open(file1, "r", encoding = "utf-8") as source:
    with open(file2, "w", encoding = "utf-8") as inheritance:
        for i in source.readlines():
            inheritance.write(i)