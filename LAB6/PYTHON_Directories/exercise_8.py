import os
import time

os.chdir(r"C:\Users\nikita k\work\LAB6\PYTHON_Directories")

with open("I_Am_Going_To_Be_Killed_Thats_Sad.txt", "a", encoding = "utf-8") as file1:
    time.sleep(10)
os.remove(r"C:\Users\nikita k\work\LAB6\PYTHON_Directories\I_Am_Going_To_Be_Deleted_Thats_Sad.txt")