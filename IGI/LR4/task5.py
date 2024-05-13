import numpy as np
from input import valid_type
from math import floor
from decorators import try_again_decorator
from statistics import median

class Matrix:
    __max_val = 100

    def __init__(self, n: int, m: int):
        self.__n = n
        self.__m = m
        self.fill_matrix(n, m)

    @property
    def matrix(self):
        return self.__A

    @property
    def n(self) -> int:
        return self.__n

    @n.setter
    def n(self, n: int):
        self.__n = n
        self.fill_matrix(self.n, self.m)

    @property
    def m(self) -> int:
        return self.__m

    @m.setter
    def m(self, m: int):
        self.__m = m
        self.fill_matrix(self.n, self.m)

    @property
    def max_val(self) -> int:
        return self.__max_val

    def fill_matrix(self, n: int, m: int):
        '''Fills matrix with random ints <= self.max_val.'''

        self.__A = np.random.randint(self.max_val, size=(n, m))

    def calc_median(self, x: float):
        '''Find vedians.'''

        arr = []
        for line in self.matrix:
            for item in line:
                if abs(item) > x:
                    arr.append(item)

        print("Arr:", arr)
        print("Count of elements > {}: {}".format(x, len(arr)))
        print("Median: ", median(arr))
        arr.sort()
        print("Median: ", (arr[floor(len(arr) / 2)] + arr[floor(len(arr) / 2 - ((len(arr) + 1) % 2))]) / 2)

    def __getitem__(self, item):
        return self.matrix[:, item]

    def __repr__(self):
        return np.array2string(self.matrix)


@try_again_decorator
def task5():
    '''Performs some operations on matrix using numpy.'''

    n = valid_type('Enter n: ', 'int')
    m = valid_type('Enter m: ', 'int')

    A = Matrix(n, m)
    print('Matrix of random ints:\n', A)
    x = valid_type('Enter x: ', 'float')
    A.calc_median(x)

