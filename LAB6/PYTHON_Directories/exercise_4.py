import os

def lines(path):
    if path.endswith(".txt"):
        counter = 0
        with open(path, encoding="utf8") as txt_file:
            for i in txt_file:
                counter += 1
        return counter
    else:
        return "Not a text file"

path = r"C:\Users\nikita k\work\LAB6\PYTHON_Directories\test1.txt"
print(lines(path)) 