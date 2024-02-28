import re

def snake_to_camel(text):
    words = re.split(r'_', text)
    camel_case_string = ''.join(word.capitalize() for word in words)
    return camel_case_string

snake_code = 'sjkdfhsdjkfh_SDJKFHSJH_jfsjFDSksdfdjh'
camel_code = snake_to_camel(snake_code)
print(camel_code)