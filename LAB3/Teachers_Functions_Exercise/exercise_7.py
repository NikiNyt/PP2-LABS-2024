def fibbonachi(number):
    if number <= 1:
        return number
    else:
        return(fibbonachi(number - 1) + fibbonachi(number - 2))
    
n = int(input())
for i in range (n):
 print(fibbonachi(i))