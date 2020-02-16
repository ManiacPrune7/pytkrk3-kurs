"""
    reprezentacja stosu
"""


class Stack:
    def __init__(self, limit=None):  # tworzy stos z dwoma atrybutami: data i length
        self.data = []
        self.length = 0
        self.limit = limit
    def push(self, value):  # dodaje element (value) na koniec
        if self.limit is None or self.length < self.limit:
            self.data.append(value)
            self.length += 1
        elif self.limit == self.length:
            print("STOS JEST PELNY!!!")
    def pop(self):  # usuwa element z konca
        if self.length > 0:
            self.data.pop()
            self.length -= 1
        else:
            print("STOS JEST PUSTY!!!")

stack = Stack()
stack.push(5)
stack.push(6)
stack.push(7)
stack.pop()
stack.pop()
stack.pop()
stack.pop()
print(stack.data)
print(stack.length)