from multiprocessing import Process
from os import getpid
from random import randint
from time import time, sleep


def task(name):
    print(f'Start... {name}')
    time_to_run = randint(1,5)
    sleep(time_to_run)
    print(f'{name} done. time used: {time_to_run}seconds')


def main():
    start = time()
    p1 = Process(target=task, args=('Python', ))
    p2 = Process(target=task, args=('Java', ))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    end = time()
    print(f'Total time: {end - start}')


if __name__ == '__main__':
    main()

