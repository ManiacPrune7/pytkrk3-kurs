"""
    iterator - petla for otrzymuje liczby od 0 do n
"""

class Counter:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return CounterIterator(self.n)


class CounterIterator:
    def __init__(self, n):
        self.n = n
        self.temp = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.temp <= self.n:
            result = self.temp
            self.temp += 1
            return result, result-1
        else:
            raise StopIteration

counter = Counter(5)

for i, j in counter:
    print(i, j)