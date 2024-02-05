def get_max(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    elif c > a and c > b:
        return c
    
num1 = int(input())
num2 = int(input())
num3 = int(input())

print("maximum og three numbers is:", get_max(num1, num2, num3))