## Think of a recursive version of the function f(n) = 3 * n, i.e. the multiples of 3
## F1=3 , F2=3+3=6 , F3=3+3+3=9 


def fun (num):
    if num==1:
        return 3
    else:
        return fun(num-1) + 3
    
print(fun(3))