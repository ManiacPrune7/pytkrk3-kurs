"""
    operacje na pliku python_zen.txt
"""


def count_lines_and_signs(file_path: str) -> tuple:

    with open(file_path) as file:

        amount_of_lines = 0
        amount_of_signs = 0

        for line in file:
            amount_of_lines += 1
            # amount_of_signs += sum([1 for sign in line if sign != " "])
            # amount_of_signs += len([sign for sign in line if sign != " "])
            amount_of_signs += len(list(filter(lambda sign: sign != " ", line)))
            # for sign in line:
            #     if sign != " ":
            #         amount_of_signs += 1

    return amount_of_lines, amount_of_signs


def replace_word(source_file: str, # python_zen.txt
                 destination_file: str, # python_zen_was.txt
                 word_to_replace: str, # is
                 replacing_word: str): # was

    with open(source_file, "r") as file:
        lines = file.readlines()

    with open(destination_file, "w") as file:
        for line in lines:
            file.write(line.replace(word_to_replace, replacing_word))


print(count_lines_and_signs(r"C:\Users\Dell Latitude E7450\SDA\pytkrk3-kurs\python_sredniozaawansowany\materialy\python_zen.txt"))
replace_word(r"C:\Users\Dell Latitude E7450\SDA\pytkrk3-kurs\python_sredniozaawansowany\materialy\python_zen.txt",
             r"C:\Users\Dell Latitude E7450\SDA\pytkrk3-kurs\python_sredniozaawansowany\materialy\python_zen_was.txt",
             "is",
             "was")