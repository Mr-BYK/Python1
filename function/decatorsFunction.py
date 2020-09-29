import time
import math


def calculate_time(func):
    def inner(*args, **kwargs):
        start = time.time()
        time.sleep(1)

        func(*args, **kwargs)
        finish = time.time()
        print("Fonskiyon " + str(finish - start) + " saniye sürdü.")
        return inner


def usalma(a, b):
    print(math.pow(a, b))


def faktoriyel(num):
    start = time.time()
    time.sleep(1)

    print(math.factorial(num))

    finish = time.time()
    print("Fonskiyon " + str(finish - start) + " saniye sürdü.")


def toplama(a, b):
    print(a + b)


usalma(2, 3)
faktoriyel(4)
toplama(89998, 4915491)