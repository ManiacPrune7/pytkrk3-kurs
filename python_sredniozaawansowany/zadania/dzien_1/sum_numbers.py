"""
    suma liczb od x do y
"""

def sum_numbers(a, b):
    temp = 0
    for i in range(a, b+1):
        temp = temp + i
        # temp += 1
    return temp
    # return sum(range(a, b+1))

print(sum_numbers(4, 8))