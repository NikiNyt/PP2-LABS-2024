import re

def split_at_upper(line):
    parts = re.findall('[A-Z][^A-Z]*', line)
    return parts

def tocamel(line):
    line = split_at_upper(line)
    return '_'.join(map(str.lower, line))

text = 'ThisIsCamleStyleString'

print(tocamel(text))