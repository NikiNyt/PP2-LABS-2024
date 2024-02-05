def filter_prime(mylist):
    for i in mylist:
        if int(i) % 2 > 0:
            print(i, "is prime")
        else:
            pass

mylist = []
amount = int(input())
for i in range (0, amount):
    element = input()
    mylist.append(element)
filter_prime(mylist)