import os
def allfiles(director):
    print(director)
    for i in director:
        print(os.listdir(i))
   
director = os.listdir(os.getcwd())
print(os.listdir(os.getcwd()))
print("-" * 50)
print(os.listdir("PYTHON_Directories"))
print("-" * 50)
allfiles(director)
