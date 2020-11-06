"""
    Prezentacja dzialania watkow dla operacji I/O.
"""


import threading
import requests
import time


def ping(url):
    res = requests.get(url)
    print(f'{url}: {res.text}')


urls = [
    'http://httpstat.us/200',
    'http://httpstat.us/400',
    'http://httpstat.us/404',
    'http://httpstat.us/408',
    'http://httpstat.us/500',
]


if __name__ == '__main__':
    start = time.time()
    for url in urls:
        ping(url)
    print(f'Sequential: {time.time() - start : .2f} seconds\n')

    start = time.time()
    threads = []
    for url in urls:
        thread = threading.Thread(target=ping, args=(url,))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()

    print(f'Threading: {time.time() - start : .2f} seconds')