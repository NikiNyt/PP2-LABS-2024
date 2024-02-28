import re

def find_sequences(text):
    sequences = re.findall('[A-Z][a-z]+', text)
    return sequences

data = 'sdkjfkjsdhfkshfksj_adjfjskdhfsdkjhf Sadsfsdf_sdf Hello World cyberpank_2077 lenovo flowers_from'

print(find_sequences(data))