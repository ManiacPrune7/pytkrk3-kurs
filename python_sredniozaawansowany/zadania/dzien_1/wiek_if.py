"""
    If na podstawie wieku
"""

def check_your_age():
    age = int(input("Tell me your age: "))  # 22

    if age >= 18:
        print("Uzytkownik pelnoletni")
        if age >= 100:
            print("200 lat!")
    else:
        print("Uzytkownik niepelnoletni")
        print(f"Do pelnoletniosci brakuje {18-age}")

check_your_age()