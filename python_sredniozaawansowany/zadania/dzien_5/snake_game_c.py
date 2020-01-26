"""
    dopisywanie wyniku do pliku
"""

import csv


def add_game(file_path: str, points: int):

    with open(file_path, "r+", newline="") as file:  # newline pomocny na windowsie (pozdrawiam)

        csvreader = csv.DictReader(file)

        index = 0
        for row in csvreader:
            index += 1

        csvwriter = csv.DictWriter(file,
                                   fieldnames=["Game Number", "Points"])

        csvwriter.writerow({"Game Number": index+1, "Points": points})


add_game(r"C:\Users\Dell Latitude E7450\SDA\pytkrk3-kurs\python_sredniozaawansowany\materialy\snake_game.csv",
         50)

