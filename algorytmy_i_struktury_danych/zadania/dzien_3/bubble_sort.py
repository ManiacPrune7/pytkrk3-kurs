"""
    sortowanie babelkowe
"""


def bubble_sort(t):

    n = len(t)-1

    while n > 0:
        for i in range(n):
            if t[i] > t[i+1]:
                t[i], t[i+1] = t[i+1], t[i]
        n -= 1
    return t


import random

a = [i for i in range(100000)]
random.shuffle(a)

bubble_sort(a)
print(a)


