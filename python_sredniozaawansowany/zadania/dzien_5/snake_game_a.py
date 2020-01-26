"""
    analiza/sortowanie wynikow z pliku snake_games.csv
"""

import csv
from typing import Union


def sort_games(file_path: str) -> Union[list, tuple]:

    with open(file_path) as  csvfile:

        csvreader = csv.DictReader(csvfile)
        games = []
        for row in csvreader:
            games.append(row)
        games.sort(key=lambda x: x["Points"])

        # temp = []
        # for game_number in games:
        #     temp.append(game_number["Game Number"])

        return [game_number["Game Number"] for game_number in games]


print(sort_games(r"C:\Users\Dell Latitude E7450\SDA\pytkrk3-kurs\python_sredniozaawansowany\materialy\snake_game.csv"))