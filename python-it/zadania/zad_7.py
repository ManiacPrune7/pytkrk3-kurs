"""

[6, 3, 5, 11, 16, 12]
min_diff = 1

[6, 3, 1, 8, 11, 20]
min_diff = 2

"""

import math
import random

def find_min_diff_n2(nums: list) -> int:
  # zdefiniowac poczatkowa najmniejsza roznice
  # iterowac po liscie
  # iterowac po liscie w sposob zagniezdzony
  # ustalac roznice pomiedzy kazdym elementem
  # zapamietywac min_diff (aktualizowac)
  # zwrocic min_diffa
  min_diff = math.inf

  for i in range(len(nums)-1):
    for j in range(i+1, len(nums)):
      # porownywanie element i - element j -> abs()
      if abs(nums[i] - nums[j]) < min_diff:
        min_diff = abs(nums[i] - nums[j])

  return min_diff

nums = list(range(100000))
random.shuffle(nums)

print(find_min_diff_n2(nums))

#
# [6, 3, 5, 11, 16, 12]
# [3, 5, 6, 11, 12, 16]
#

def find_min_diff_nlogn(nums: list) -> int:
  # zdefiniowac poczatkowa najmniejsza roznice
  # iterowac po liscie
  # iterowac po liscie w sposob zagniezdzony
  # ustalac roznice pomiedzy kazdym elementem
  # zapamietywac min_diff (aktualizowac)
  # zwrocic min_diffa
  min_diff = math.inf
  nums = sorted(nums)

  for i in range(len(nums)-1):
    # porownywanie element i - element j -> abs()
    if abs(nums[i] - nums[i+1]) < min_diff:
      min_diff = abs(nums[i] - nums[i+1])

  return min_diff

print(find_min_diff_nlogn(nums))
