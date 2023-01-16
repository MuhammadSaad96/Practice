# Write a recursive Python function that returns the sum of the first n integers. 
# (Hint: The function will be similiar to the factorial function!)
# 0 = 0
# 1 = 1
# 2 = 2+1 = 3
# 3 = 3+2+1 = 6
# 4 = 4+3+2+1 = 10
# 5 = 5+4+3+2+1 = 13


def fun (num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return num + fun(num-1)

print(fun(4))