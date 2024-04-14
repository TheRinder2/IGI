import random


def generator(n):
    for _ in range(n):
        yield random.uniform(-10, 10)
