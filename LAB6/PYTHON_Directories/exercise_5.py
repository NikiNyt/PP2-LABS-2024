import os

def writeinfile(filename, list):
    with open(filename, "w", encoding = "utf-8") as output:
        for i in list:
            output.write(i + "\n")

os.chdir(r"PYTHON_Directories")
amount = int(input())

list = []

for i in range (0, amount):
    list.append(str(input()))

writeinfile("write_here.txt", list)
print("Code executed successfully")

