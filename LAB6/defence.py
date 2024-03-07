import os
import re
text = ""
with open("textovik.txt", "w", encoding = "utf-8") as tx:
    tx.write("SDdsfhskdfh 2.0 sdfhs2.55kfhjsdhka 5.11")
with open("textovik.txt", "r", encoding = "utf-8") as tx:
    pattern = r"\d*\.\d*"
    for i in tx:
        text = text + i
    answer = re.findall(pattern, text)
print(answer)

