"""
    funkcja obliczajaca wartosc liczby pi
"""

import random
import math

def get_pi():

    circle_points = 0
    square_points = 0

    for i in range(10000000):
        x = random.random() * 2
        y = random.random() * 2

        if (x-1)**2 + (y-1)**2 <= 1:
            circle_points += 1
            square_points += 1
        else:
            square_points += 1

    return 4*circle_points/square_points

print(get_pi())
print(math.pi)