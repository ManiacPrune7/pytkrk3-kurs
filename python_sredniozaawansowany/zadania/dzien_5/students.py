"""
    analiza pliku students.csv
"""

import csv


def find_tallest_students(file_path: str) -> tuple:

    with open(file_path, "r") as csvfile:
        # wykorzystac csv.reader
        csvreader = csv.reader(csvfile, delimiter=",")
        # dwie zmienne tymczasowe (wzrostM, imieM), (wzrostK, imieK)
        student_m = ["", 0]
        student_w = ["", 0]
        for row in csvreader:
        # wyprintowac row w petli for (w celach sprawdzajacych)
            # print(row)
        # przechodzimy po wszystkich liniach
        # stosujemy algorytm na wyszukiwanie max wartosci
            if row[1] == "M":
                # print(row)
                if int(row[2]) > student_m[1]:
                    student_m[1] = int(row[2])
                    student_m[0] = row[0]
            else:
                if int(row[2]) > student_w[1]:
                    student_w[1] = int(row[2])
                    student_w[0] = row[0]

        return student_m[0], student_w[0]


print(find_tallest_students(r"C:\Users\Dell Latitude E7450\SDA\pytkrk3-kurs\python_sredniozaawansowany\materialy\students.csv"))