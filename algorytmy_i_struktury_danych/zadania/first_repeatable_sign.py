"""
    Funkcja znajdujaca pierwszy powtarzajacy sie znak
"""


def find_first_repeatable_sign(string: str):

    temp = set()

    # for i in range(len(string)):
    #     i # a k a p i t
    #     string[i] # k
    for letter in string:
        if letter not in temp:
            temp.add(letter)
        else:
            return letter

print(find_first_repeatable_sign("asdfgh"))
