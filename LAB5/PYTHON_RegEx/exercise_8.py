import re

def split_at_upper(line):
    parts = re.findall('[A-Z][^A-Z]*', line)
    return parts

string = "AsjdfhsjhfIsdjfhsjdhfsNsdjfhsAk"
print(split_at_upper(string))