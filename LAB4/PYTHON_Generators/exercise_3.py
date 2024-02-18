def divisibility(a):
    i = 0
    while i <= a:
     if i % 3 == 0 and i % 4 == 0:
        yield i
        i += 1
     else:
        i += 1

n = int(input())
gen = divisibility(n)
for i in gen:
   print(i)