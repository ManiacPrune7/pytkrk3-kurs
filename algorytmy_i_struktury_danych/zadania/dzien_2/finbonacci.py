"""
    implementacja ciagu Fibonacciego z wykorzystaniem rekurencji
"""

def fibo_iter(n):
    #a, b = 0, 1 <- tak tez mozna
    a = 0
    b = 1
    for i in range(n-1):
        a, b = b, a+b
    return b


def fibo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibo(n-1) + fibo(n-2)

print(fibo(40))