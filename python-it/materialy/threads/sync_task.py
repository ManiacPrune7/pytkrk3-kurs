"""
    Problemy z synchronizacja - race condition.
"""

import threading


class Thread(threading.Thread):
    def __init__(self, t, *args):
        super().__init__(target=t, args=args)
        self.start()


counter = 0


def increment():
    global counter
    counter += 1


def inc_a():
    for _ in range(100000):
        increment()


def main():
    t1 = Thread(inc_a)
    t2 = Thread(inc_a)

    t1.join()
    t2.join()


if __name__ == '__main__':
    main()
    print(counter)
