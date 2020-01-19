"""
    generator liczb parzystych
"""


def liczby():
    for i in range(4):
        yield i * 2


for parzysta in liczby():
    print(parzysta)
