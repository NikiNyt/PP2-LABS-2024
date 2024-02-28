import re

testik = ["a", "ab", "abb", "abbb", "ac", "b", "bb"]

for answer in testik:
    pattern = 'ab{2,3}'
    if re.match(pattern, answer):
        print(answer)