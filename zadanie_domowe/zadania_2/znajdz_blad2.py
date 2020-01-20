"""
    Twoim zadaniem jest znalezienie bledu w napisanej funkcji.
    Funkcja powinna obliczac sume elementow z listy liczb, jednakze
    nie robi tego poprawnie.
    Przejrzyj jej cialo i zastanow sie, gdzie zostal popelniony blad.
    Mozna zmienic tylko jedna linijke. W funkcji nie brakuje niczego,
    nie ma potrzeby pisac nowych linii kodu.
    Funkcje proponuje przetestowac na zbiorach:
    a = [0, 1, 2, 3, 4, 5]
    b = [1, 2, 3, 4, 5]
    c = [100, 1, 2, 3, 100]
"""


def compute_sum(numbers):
    ans = 0
    for i in range(1, len(numbers)):
        ans = ans + numbers[i]
    return ans
