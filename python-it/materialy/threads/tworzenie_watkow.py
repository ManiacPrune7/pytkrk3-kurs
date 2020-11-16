"""
    Tworzenie watkow.
"""

import time
import threading


def iterate_print(iterable):
    """Funkcja wypisujaca elementy listy."""
    for item in iterable:
        # time.sleep(0.1)
        print(item)


# tworzenie watkow
t1 = threading.Thread(target=iterate_print, args=(range(5),))
t2 = threading.Thread(target=iterate_print, args=("Python",))

start = time.perf_counter()
iterate_print(range(5))
iterate_print("Python")
print('Took: % seconds.' % (time.perf_counter() - start))
# uruchomienie watkow
start = time.perf_counter()
t1.start()
t2.start()

# czekanie z wykonaniem dalszego kodu, az oba watki sie zakoncza
t1.join()
t2.join()

print('Took: % seconds.' % (time.perf_counter() - start))
print("Done!")
