def evens(a):
    i = 0
    while i <= a:
     if i % 2 == 0:
        yield i
        i += 1
n = int(input())
gen = evens(n)
for i in gen:
   print(i)