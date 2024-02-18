def squares(a, b):
    i = a
    while i <=b:
        yield i*i
        i += 1

a = int(input())
b = int(input())
gen = squares(a, b)

for i in gen:
    print(i)