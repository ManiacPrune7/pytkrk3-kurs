"""
    dekorator wypisujacy argumenty
"""


def print_arguments(function):

    def wrapper(*args, **kwargs):  # 1, 2, 3, a=1, b=2, c=3
        print(f"Argumenty: {args} i {kwargs}")
        x = function(*args, **kwargs)
        print(f"Wykonano z {len(args) + len(kwargs)} argumentami")
        return x
    return wrapper


@print_arguments
def hello_world():
    print("Hello, World!")


@print_arguments
def add(a, b):
    return a+b

hello_world()
print(add(a=4, b=5))