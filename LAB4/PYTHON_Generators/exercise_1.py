def squares(a):
    i = 1
    while i <= a:
        yield i*i
        i += 1

n = int(input())
gen = squares(n)
for i in gen:
    print(i)
    