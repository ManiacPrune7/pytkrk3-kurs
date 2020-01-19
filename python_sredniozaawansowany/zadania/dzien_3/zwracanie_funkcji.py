"""
Przyklad zwracania funkcji z funkcji.
"""

def greeting(time: str):

    def goodday(name):
        return "Trzy bobry, " + name

    def goodnight(name):
        return "Dobranoc, " + name

    if time == "morning":
        return goodday
    elif time == "night":
        return goodnight
    else:
        print("ZLY ARGUMENT")

dzien_dobry = greeting("morning")
print(dzien_dobry.__name__)
print(dzien_dobry("Radoslaw"))

# dzien_dobry = greeting("morning")("Radoslaw")