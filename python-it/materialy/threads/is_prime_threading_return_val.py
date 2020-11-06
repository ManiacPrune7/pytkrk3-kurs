"""
    Przyklad wielowatkowej pracy nad liczeniem liczb pierwszych.
    Wartosc jest zwracana z watkow.
"""

import threading
import time
from math import sqrt


class MyThread(threading.Thread):
  def __init__(self, x):
    super().__init__()
    self.x = x
    self.result = None

  def run(self):
    # print('Starting processing %i...' % self.x)
    self.result = is_prime(self.x)


def is_prime(x):
  if x < 2:
    return False
  if x == 2:
    return True
  if x % 2 == 0:
    return False
  limit = int(sqrt(x)) + 1
  for i in range(3, limit, 2):
    if x % i == 0:
      return False
  return True


# sequential
start = time.perf_counter()
result = []
my_input = [i for i in range(10 ** 13, 10 ** 13 + 500)]
for i in my_input:
  if is_prime(i):
    result.append(i)
print('Result 1:', result)
print('Took: %.2f seconds.' % (time.perf_counter() - start))

# multithreaded

my_input = [i for i in range(10 ** 13, 10 ** 13 + 500)]
threads = []
result = []
start = time.perf_counter()
for z in my_input:
  temp_thread = MyThread(z)
  temp_thread.start()
  threads.append(temp_thread)

for thread in threads:
  thread.join()

for thread in threads:
  if thread.result:
    result.append(thread.x)

print('Took: %.2f seconds.' % (time.perf_counter() - start))
print('Result 2:', result)
print('Finished.')