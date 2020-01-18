"""
    rzutowanie znaku na liczbe z tablicy ascii
"""

def sign_to_digit(string):
    for letter in string:  # python
        print(f"ord(letter) = {ord(letter)} a letter = {letter}")

sign_to_digit("Python")