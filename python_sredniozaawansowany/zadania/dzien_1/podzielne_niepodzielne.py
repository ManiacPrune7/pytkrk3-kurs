"""
    Ciag liczb podzielnych przez 7 a niepodzielnych przez 5,
    dla liczb od 2000 do 3200
"""

# x % 5 == 0 (jeżeli True, to liczba jest podzielna przez 5)
# x % 5 != 0 (jeżeli True, to liczba nie dzieli się przez 5)

# zakres od x do y: range(x, y)

def find_numbers(a, b):
    numbers = []
    for number in range(a, b+1):
        if number % 7 == 0 and number % 5 != 0:
            numbers.append(number)
    return numbers

print(find_numbers(2000, 3200))