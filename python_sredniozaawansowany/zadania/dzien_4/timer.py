"""
    jak dlugo wykonuje sie funkcja - dekorator
"""

import time


def timer(function):

    def wrapper(*args, **kwargs):
        # rozpoczeli liczeni
        start_time = time.perf_counter()
        # wywolali funkcje
        result = function(*args, **kwargs)
        # zakonczyli liczenie
        end_time = time.perf_counter()
        # wypisali czas dzialania
        print(end_time-start_time)
        # zwrocili wartosc zwracana przez funkcje
        return result

    return wrapper


@timer
def hello_world():
    time.sleep(1)
    print("Hello, World!")

hello_world()