def find_common_elements(list1, list2):
    mylist3 = []
    for i in list1:
        for x in list2:
            if x == i:
                mylist3.append(x)
    return mylist3


mylist1 = []
mylist2 = []
amount1 = int(input())
for i in range (0, amount1):
    element = input()
    mylist1.append(element)
amount2 = int(input())
for i in range (0, amount2):
   element = input()
   mylist2.append(element)
print(find_common_elements(mylist1, mylist2))