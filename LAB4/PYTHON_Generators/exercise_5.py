def numbers_till0(n):
    i = n
    while i >= 0:
        yield i
        i -= 1

n = int(input())
gen = numbers_till0(n)

for i in gen:
    print(i)