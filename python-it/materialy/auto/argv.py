"""
  przekazywanie argumentow z terminala do pliku
"""

import sys


def print_all_params(*params):
  print(*params)


if __name__ == '__main__':
  print(f'Nazwa pliku: {sys.argv[0]}')
  print_all_params(sys.argv[1:])