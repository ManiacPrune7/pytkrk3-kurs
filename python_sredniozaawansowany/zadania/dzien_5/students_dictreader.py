"""
    analiza pliku students.csv
"""

import csv


def find_tallest_students(file_path: str) -> tuple:

    with open(file_path, "r") as csvfile:
        # wykorzystac csv.reader
        csvreader = csv.DictReader(csvfile, fieldnames=["name", "gender", "height", "weight"])
        # dwie zmienne tymczasowe (wzrostM, imieM), (wzrostK, imieK)
        student_m = {"name": "", "height": 0}
        student_w = {"name": "", "height": 0}
        for row in csvreader:
            if row["gender"] == "M":
                if int(row["height"]) > student_m["height"]:
                    student_m["height"] = int(row["height"])
                    student_m["name"] = row["name"]
            else:
                if int(row["height"]) > student_w["height"]:
                    student_w["height"] = int(row["height"])
                    student_w["name"] = row["name"]

        return student_m["name"], student_w["name"]


print(find_tallest_students(r"C:\Users\Dell Latitude E7450\SDA\pytkrk3-kurs\python_sredniozaawansowany\materialy\students.csv"))