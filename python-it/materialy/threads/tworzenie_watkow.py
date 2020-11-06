"""
    Tworzenie watkow.
"""

import threading


def iterate_print(iterable):
    """Funkcja wypisujaca elementy listy."""
    for item in iterable:
        print(item)


# tworzenie watkow
t1 = threading.Thread(target=iterate_print, args=(range(5),))
t2 = threading.Thread(target=iterate_print, args=("Python",))

# uruchomienie watkow
t1.start()
t2.start()

# czekanie z wykonaniem dalszego kodu, az oba watki sie zakoncza
t1.join()
t2.join()

print("Done!")
