"""
    Odliczanie do 0 przez dwa procesy.
"""

from multiprocessing import Process
import time


def count_down(name, delay):
    print('Process %s starting...' % name)

    counter = 5

    while counter:
        for _ in range(10000000):
            pass
        print('Process %s counting down: %i...' % (name, counter))
        counter -= 1

    print('Process %s exiting...' % name)


if __name__ == '__main__':
    process1 = Process(target=count_down, args=('A', 0.5))
    process2 = Process(target=count_down, args=('B', 0.5))

    x = time.perf_counter()
    process1.start()
    process2.start()

    process1.join()
    process2.join()
    print(time.perf_counter()-x)
    print('Done.')