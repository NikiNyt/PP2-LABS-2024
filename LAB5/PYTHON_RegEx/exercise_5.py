import re

def math_pattern(text):
    if re.search('a.*b$', text):
        return True
    return False

testik = ["acdb", "ab", "abbbbb", "acb", "abbbb", "assdfee", 'ssffaaeeefb']
for l in testik:
    if math_pattern(l):
        print(l)