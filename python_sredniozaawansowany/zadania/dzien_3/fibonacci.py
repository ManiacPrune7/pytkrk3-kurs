"""
    funkcje zwracajace liczby ciagu Fibonacciego;
    wersja iteracyjna i z generatorem
"""


def fibo_i(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

a = fibo_i(5)
print(a)


def fibo_g(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

g = fibo_g(10)
for i in g:
    print(i)