import re

testik = ["a", "sfkgjsf", "ababab", "sfjgkdfjgabbbbbhghjghjgk"]

for line in testik:
    pattern = r'ab*'
    if re.search(pattern, line):
        print(line)
