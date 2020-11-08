"""
1. Obliczyć sumę cyfr w liczbie.
2. Obliczyć sumę cyfr w liczbie algorytmicznie i wykorzystując rekurencję.
"""

import unittest

def count_sum_of_digits(num: int) -> int:
  # string = str(num) # '1234'
  # temp = []
  # for sign in string:
  #   temp.append(int(sign))  # ['1', '2', '3', '4'] -> [1, 2, 3, 4]
  # return sum(temp)
  return sum([int(sign) for sign in str(num)])  # return sum([1, 2, 3, 4])

def count_sum_of_digits_rec(num: int) -> int:
  digit_sum = num % 10
  if num:
    return digit_sum + count_sum_of_digits_rec(num//10)
  else:
    return digit_sum

#print(count_sum_of_digits(1234))  # 10 1+2+3+4=10
#print(count_sum_of_digits_rec(1234))  # 10 1+2+3+4=10

class TestCountOfDigits(unittest.TestCase):

  def test_1234(self):
    result = count_sum_of_digits_rec(1234)
    self.assertEqual(result, 10)

  def test_0(self):
    result = count_sum_of_digits_rec(0)
    self.assertEqual(result, 0)

  def test_10(self):
    result = count_sum_of_digits_rec(10)
    self.assertEqual(result, 1)


if __name__ == '__main__':
  unittest.main()