import re

def find_sequences(text):
    sequences = re.findall('[a-z]+_[a-z]+', text)
    return sequences

data = 'sdkjfkjsdhfkshfksj_adjfjskdhfsdkjhf Sadsfsdf_sdf Hello World cyberpank_2077 lenovo flowers_from'

for line in find_sequences(data):
    print(line)