"""
    sortowanie przez wybór
"""

def find_min(array: list):
    index = 0
    temp_min = array[index]
    for i, element in enumerate(array):
        if element < temp_min:
            temp_min = element
            index = i
    return index, temp_min


def selection_sort(nums):
    n = len(nums)
    for i in range(n):
        index, num = find_min(nums[i:])
        index += i
        nums[i], nums[index] = nums[index], nums[i]


import random
a = [i for i in range(100000)]
random.shuffle(a)
selection_sort(a)
print(a)