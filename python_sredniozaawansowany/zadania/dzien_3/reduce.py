"""
    wyliczanie iloczynu liczb w liscie za pomoca:
    a) petli for
    b) funkcji reduce
"""

from functools import reduce

# a)

def mult_for(numbers: list) -> int:
    temp = 1
    for number in numbers:
        temp *= number  # temp = temp * number
    return temp


# b)

def mult_reduce(numbers: list) -> int:
    return reduce(lambda x, y: x*y, numbers)


nums = [1,2,3,4,5]

print(mult_for(nums))
print(mult_reduce(nums))