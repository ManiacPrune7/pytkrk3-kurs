"""
    obliczanie wartosci sredniej dla ilosc punktow
"""

import csv


def count_mean_points(file_path: str) -> float:

    with open(file_path) as file:

        csvreader = csv.DictReader(file)
        points = 0
        n = 0

        for game in csvreader:
            points += int(game["Points"])
            n += 1

        return points/n


print(count_mean_points(r"C:\Users\Dell Latitude E7450\SDA\pytkrk3-kurs\python_sredniozaawansowany\materialy\snake_game.csv"))