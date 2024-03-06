def uppercases(s):
    uppers = 0
    for i in s:
        if i.isupper() == True:
            uppers = uppers + 1
    return uppers

def lowercases(s):
    lowers = 0
    for i in s:
        if i.islower() == True:
            lowers = lowers + 1
    return lowers


s = input()
print("Upper case letters:", uppercases(s))
print("Lower case letters:", lowercases(s))