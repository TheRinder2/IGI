import random


def generator(n):
    """
    Generate list size of n
    """
    for _ in range(n):
        yield random.uniform(-10, 10)
