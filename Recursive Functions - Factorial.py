## Recursive Functions Exercise
## factorial in Python
# 0! = 1
# 1! = 1
# 2! = 2*1 = 2
# 3! = 3*2*1 = 6
# 4! =  4*3*2*1 = 24
# 5! = 5*4*3*2*1 = 120

def factorial(num):
    if (num == 0 or num ==1):
        return 1
    else:
        return num * factorial(num-1)
        

print(factorial(5))