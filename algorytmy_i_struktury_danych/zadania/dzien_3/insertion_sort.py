"""
    sortowanie przez wstawianie
"""

def insert_sort(d):
    n = len(d) - 1
    j = n - 1

    while j >= 0:
        x = d[j]
        i = j + 1

        while i <= n:
            if x <= d[i]:
                break
            else:
                d[i-1] = d[i]
                i = i + 1
        d[i-1] = x
        j = j - 1

import random
a = [i for i in range(100000)]
random.shuffle(a)

insert_sort(a)
print(a)