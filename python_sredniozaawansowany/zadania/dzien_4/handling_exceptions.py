"""
    wylapywanie wlasnych wyjatkow
"""

# definicja czterech wlasnych wyjatkow
class StrArgTypeError(Exception):
    pass

class BoolArgTypeError(Exception):
    pass

class NumberArgTypeError(Exception):
    pass

class LenGreaterThanOneError(Exception):
    pass


# napisac funkcje sprawdzajaca typ jedynego argumentu
def check_type(arg):
    if arg is None:
        print("None is okay")
    elif type(arg) is str:
        raise StrArgTypeError
    elif type(arg) is bool:
        raise BoolArgTypeError
    elif type(arg) is int or type(arg) is float:
        raise NumberArgTypeError
    elif len(arg) > 1:
        raise LenGreaterThanOneError

# powinna ona zwracac wyjatki (dzialac) zgodnie z trescia zadania

# stworzyc if __name__ == "__main__":
if __name__ == "__main__":
    try:
        check_type(1)
    except StrArgTypeError:
        print("Argument byl stringiem")
    except BoolArgTypeError:
        print("Argument byl boolem")
    except NumberArgTypeError:
        print("Argument byl liczba")
    except LenGreaterThanOneError:
        print("Argument byl dluzszy niz 1")
    finally:
        print("JUHUUUUU")
# w tym bloku: try-except
# w bloku try wywolujemy nasza funkcje
# 4x except TypBledu:
# instrukcje w blokach except zgodnie z zadaniem