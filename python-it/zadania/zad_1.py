"""
Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 3200 and 3300 (both included).
The numbers obtained should be printed in a comma-separated on a single line.

Napisz prosty program (funkcja), ktory znajdzie wszystkie liczby, ktore sa podzielne przez 7 ale nie sa wielokrotnoscia liczby 5
(zakres: 3200 - 3300, obydwie liczby wliczaja sie do tego zakresu).
Funkcja powinna wypisac wszystkie liczby w jednej linii oddzielajac je przecinkiem.
"""

def print_numbers():
  nums = []
  for num in range(3200, 3301):
    if num % 7 == 0 and num % 5 != 0:
      nums.append(str(num))  # '3262'
  print(','.join(nums))


def print_numbers_2():
  print(','.join([str(num) for num in range(3200, 3301) if num % 7 == 0 and num % 5 != 0]))

print_numbers()
print_numbers_2()

