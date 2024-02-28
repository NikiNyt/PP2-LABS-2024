import re

def spaces(text):
    pattern = r'([A-Z][^A-Z]*)'
    space_add = re.sub(pattern, r' \1', text)
    return space_add

text = "KsdfjsfsdfueIsdfjshdfskjKhsdfhsfs"
answer = spaces(text)
print(answer)