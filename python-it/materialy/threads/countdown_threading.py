"""
    Odliczanie do 0 przez dwa watki.
"""

import time
import threading


class MyThread(threading.Thread):
    def __init__(self, name, delay):
        super().__init__()
        self.name = name
        self.delay = delay

    def run(self):
        print('Starting thread %s.' % self.name)
        count_down(self.name, self.delay)
        print('Finished thread %s.' % self.name)


def count_down(name, delay):
    counter = 5

    while counter:  # != 0
        # time.sleep(delay)
        for _ in range(10000000):
            pass
        print(f'Thread {name} counting down: {counter}...')
        counter -= 1


thread1 = MyThread('A', 0.5)
thread2 = MyThread('B', 0.5)
x = time.perf_counter()
thread1.start()
thread2.start()

thread1.join()
thread2.join()
print(time.perf_counter()-x)
print('Finished.')
