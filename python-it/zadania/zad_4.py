"""
  Zadania z  palindromami.
  1. Funkcja sprawdzajaca czy napis jest palindromem.
  2. Funkcja sprawdzajaca czy napis jest palindromem w sposob algorytmiczny.
  3. Napisz funkcję przyjmującą napis i sprawdzajacą czy z podanych liter (wszystkich) można utworzyć palindrom.
"""

import collections

def is_palindrome_permutation(string: str) -> bool:
  # 1
  # temp_str = ''  #
  # for sign in string:
  #   if sign != ' ':
  #     temp_str += sign
  # temp_list = []  # ['a', 'b', 'c', 'd']

  # for sign in string:
  #   if sign != ' ':
  #     temp_list.append(sign)
  # string = ''.join(temp_list)

  string = ''.join(string.split())

  # 2
  # temp_dict = {}
  # for sign in string:
  #   if sign not in temp_dict:  # temp_dict.keys()
  #     temp_dict[sign] = 1
  #   else:
  #     temp_dict[sign] += 1

  # temp_dict = collections.defaultdict(int)  # int -> 0, float -> 0.0, list -> []
  # for sign in string:
  #   temp_dict[sign] += 1

  temp_dict = collections.Counter(string)

  # 3
  odd_count = 0
  for amount in temp_dict.values():
    if amount % 2 != 0:
      odd_count += 1

  return not odd_count > 1


print(is_palindrome_permutation('ja t ak'))  # kajak

def is_palindrome(string: str) -> bool:
  return string == string[::-1]


def is_palindrome_alg(string: str) -> bool:
  for i in range(len(string)//2):  # 0 1
    if string[i] != string[-(1+i)]:
      return False
  return True


def is_palindrome_alg2(string: str) -> bool:
  left_index = 0
  right_index = -1

  while left_index < len(string)//2:
    if string[left_index] != string[right_index]:
      return False
    else:
      left_index += 1
      right_index -= 1
  return True

#print(is_palindrome_alg2('cokolwiek'))

