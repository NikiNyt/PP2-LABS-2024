import os
import time

alphabet = "ABCDEFGHIJKLMOPQRSTUVWXYZ"

for i in alphabet:
    if os.path.exists(i + ".txt") == False:
      with open(i + ".txt", "w", encoding = "utf-8"):
          pass

time.sleep(10)

for i in alphabet:
    if os.path.exists(i + ".txt") == True:
      os.remove(i + ".txt")