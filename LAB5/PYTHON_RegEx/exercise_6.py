import re

def double_dot(text):
    new_text = re.sub(r'[ ,.]', ':', text)
    return new_text

string = "shkdfshdfk ah,ыва,12313123123123., sdhfsdhfsdf 112u834 SKJHFKSJDHF_SJHDFsdjfhjsdf1238734yrdak,."
print(double_dot(string))