"""
    silnia rekurencyjnie
"""


def factorial_iter(n):
    silnia = 1

    for i in range(1, n+1):
        silnia *= i

    return silnia


def factorial(n):
    if n == 0 or n == 1:
        return 1
    return factorial(n-1) * n


print(factorial_iter(5))
print(factorial(5))