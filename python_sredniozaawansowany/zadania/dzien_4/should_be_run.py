"""
    jak "wylaczyc" i "wlaczyc" funkcje za pomoca dekoratora
"""

SHOULD_BE_RUN = False  # True


def should_be_run(func):

    def wrapper(*args, **kwargs):
        # sprawdz czy SHOULD BE RUN jest na True
        if SHOULD_BE_RUN is True:
            return func(*args, **kwargs)
        else:
            print("Pomijam...")
        # jesli tak - uruchom func i zwroc jej wartosc
        # jesli nie - wypisz "Pomijam..."

    return wrapper


@should_be_run
def hello_world():
    print("Hello, World!")


hello_world()