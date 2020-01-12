"""
    Reprezentacja danych osobowych
"""

imie = "Henryk"
nazwisko = "Walezy"
wiek = 50
email = "henrykw111@elekcja.com"
phone = "750 000 100"

def generate_data_list(imie, nazwisko, wiek, email, phone):
    return [imie, nazwisko, wiek, email, phone]

dane  = generate_data_list(imie, nazwisko, wiek, email, phone)
IMIE_POZYCJA = 0
NAZWISKO_POZYCJA = 1
dane[NAZWISKO_POZYCJA]

def generate_data(imie, nazwisko, wiek, email, phone):
    return {
        "imie": imie,
        "nazwisko": nazwisko,
        "wiek": wiek,
        "email": email,
        "phone": phone
    }

print(generate_data(imie, nazwisko, wiek, email, phone))