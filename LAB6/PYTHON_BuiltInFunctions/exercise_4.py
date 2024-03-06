import time

def square_root(num):
    return float(num ** .5)

delay = int(input())
number = int(input())
time.sleep(delay / 1000)
print("Square root of", number, "after", delay, "miliseconds is", square_root(number))