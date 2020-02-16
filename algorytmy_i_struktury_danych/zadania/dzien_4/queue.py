"""
    reprezentcja kolejki
"""

from collections import deque

class FifoQueue:
    def __init__(self):  # dwa atrybuty: data oraz length
        self.data = deque()
        self.length = 0
    def append(self, value):  # dopisywanie value do kolejki (data)
        self.data.append(value)
        self.length += 1
    def pop(self):  # usuwanie najwczesniej dodanego elementu z kolejki
        if self.length > 0:
            self.data.popleft()
            self.length -= 1
        else:
            print("KOLEJKA JEST PUSTA!!!")
    def print(self):
        print(list(self.data))

fifo = FifoQueue()
fifo.append(1)
fifo.append(2)
fifo.append(3)
fifo.pop()
fifo.print()
