class Element:
    def __init__(self, data):
        self.data = data
        self.next = None


class List:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def add_element(self, element):
        if self.head is None:
            self.head = element
            self.tail = element
        else:
            self.tail.next = element
            self.tail = element
        self.count += 1

    def remove_element(self, data):
        prev = None
        act = self.head
        if act.data == data:
            self.head = act.next
            self.count -= 1
            return
        prev = act
        act = act.next
        while act is not None:
            if act.data == data:
                if act is self.tail:
                    self.tail = prev
                prev.next = act.next
                self.count -= 1
                break
            else:
                prev = act
                act = act.next

    def print_data(self):
        elem = self.head
        while True:
            print(elem.data, end=" ")
            if elem.next is None:
                break
            elem = elem.next

L = List()
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)
e5 = Element(5)
L.add_element(e1)
L.add_element(e2)
L.add_element(e3)
L.add_element(e4)
L.add_element(e5)
L.print_data()
print()
#print(L.count)
L.remove_element(5)
L.print_data()
L.remove_element(1)
print()
L.print_data()
print()
print(L.count)
print()
print(L.tail.data)
