## Recursive Functions Exercise
## Fibonacci in Python
## 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ..
## F0 = 0 , F1 = 1 , F2 = 1 , F3 = 2 , F4 = 3
## sum of last two numbers is next number

def fib(num):
    if num==0:
        return 0
    elif num==1:
        return 1
    else:
        return fib(num-1) + fib(num-2)

print(fib(10))