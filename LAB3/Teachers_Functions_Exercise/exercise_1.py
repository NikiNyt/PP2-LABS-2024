def calculate_factorial(number):
    if number == 1:
        return number
    else:
        return number * calculate_factorial(number - 1)
num = int(input())
print(calculate_factorial(num))