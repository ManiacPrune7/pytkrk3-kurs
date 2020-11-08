def extend_list(val, lst=None):
    if lst is None:
        lst = []
    lst.append(val)
    return lst

list1 = extend_list(10)  # [10]
print("list1 = ", list1)
list2 = extend_list(123, [1, 2])  # [1, 2, 123]
print("list2 = ", list2)
list3 = extend_list('a')  # ['a']
print("list3 = ", list3)
print("")
print("list1 = ", list1)
print("list2 = ", list2)
print("list3 = ", list3)

def jakas_funkcja(a, b=1, c=2):
  ...

jakas_funkcja(1)
jakas_funkcja(1, 2)
jakas_funkcja(1, b=2)
jakas_funkcja(1, 2, 3)
jakas_funkcja(1, 2, c=3)
jakas_funkcja(a=1, b=2, c=3)