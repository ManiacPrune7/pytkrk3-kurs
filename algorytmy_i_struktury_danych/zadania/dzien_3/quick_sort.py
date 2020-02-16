"""
    sortowanie szybkie
"""

def qs(t):
    L = 0
    P = len(t)-1

    def quick_sort(t, L, P):
        i = L
        j = P
        x = t[(L+P)//2]

        while i < j:
            while t[i] < x:
                i += 1
            while x < t[j]:
                j -= 1
            if i <= j:
                t[i], t[j] = t[j], t[i]
                i += 1
                j -= 1
            if L < j:
                quick_sort(t, L, j)
            if i < P:
                quick_sort(t, i, P)

    return quick_sort(t, L, P)

a = [1,6,3,8,2,6]
qs(a)
print(a)