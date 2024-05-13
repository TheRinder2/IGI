import math
from statistics import mean, median, mode, variance, covariance
from matplotlib import pyplot as plt
import numpy as np
from input import valid_type
from decorators import try_again_decorator


MAX_ITERS = 500


class LnSeries:
    max_iters = 500

    def __init__(self, x: float, eps=1e-6):
        self.x = x
        self.eps = eps
        self.series, math_value, self.n = self.calculate_series(x, eps)

        if (math.fabs(math_value - sum(self.series)) > eps):
            print('Outcome error > eps!')

    @classmethod
    def calculate_series(cls, x:float, eps=1e-6):
        '''Calculates series expansion of ln() in given point and with given error.'''

        if (math.fabs(x) <= 1):
            return 0, 0, 0

        math_value, series_value, series, iters = math.log((x + 1) / (x - 1)), 0, [], 0
        while (math.fabs(math_value - series_value) > eps and iters <= cls.max_iters):
            value = 2 / (2 * iters + 1) / (x ** (2 * iters + 1))
            series_value += value
            series.append(value)
            iters += 1

        return series, math_value, iters

    def mean(self):
        '''Calculates mean of sequence.'''
        return mean(self.series)

    def median(self):
        '''Calculates median of sequence.'''
        return median(self.series)

    def mode(self):
        '''Calculates mode of sequence.'''
        return mode(self.series)

    def variance(self):
        '''Calculates variance of sequence.'''
        return variance(self.series)

    def covariance(self):
        '''Calculates covariance of sequence.'''
        return covariance(self.series, self.series)

    @classmethod
    def plot(cls, x0: float, x1: float, file_name='plot.png'):
        '''Plots ln on [x0; x1] using series expansion and math.log() function and saves result in file_name file.'''

        xs = np.linspace(x0, x1, 10000)
        ys = [sum(cls.calculate_series(x)[0]) for x in xs]
        fig = plt.figure()
        plt.plot(xs, ys, color='red', label='Series')
        ys = [math.log((x + 1) / (x - 1)) for x in xs]
        plt.plot(xs, ys, color='blue', label='Math')
        plt.title('Ln((1+x) / (1-x))')
        plt.xlabel('x')
        plt.text(x0, sum(cls.calculate_series(x1)[0]), 'Plots ln() using series expansion and math.log() function.')
        plt.legend()
        fig.savefig(file_name)
        plt.show()


@try_again_decorator
def task3():
    '''Calculates ln((x+1)/(x-1)) using series expansion and math.log() function. Plots relevant graphics.'''

    x = valid_type('\nEnter x: ', 'float')
    eps = valid_type('Enter eps: ', 'float')
    try:
        calculate_ln(x, eps)

        x0 = valid_type('Enter left border of diapason: ', 'float')
        x1 = valid_type('Right border: ', 'float')

        LnSeries.plot(x0, x1)

        series = LnSeries(x, eps)
        print(f'Mean: {series.mean()}')
        print(f'Mode: {series.mode()}')
        print(f'Median: {series.median()}')
        print(f'Variance: {series.variance()}')

    except ValueError as err:
        print(f'ValueError: {err}')


def calculate_ln(x: float, eps=1e-6):
    """Сalculates ln() using power series expansion and the math module, as well as number of terms needed to achieve specified accuracy eps.

    Position argument:
    x -- the point.

    Keyword argument:
    eps -- the error value (default 1e-6)."""

    if (math.fabs(x) <= 1):
        raise ValueError('|x| should be more than 1!')

    math_value = math.log((x + 1) / (x - 1))

    series_value, n = 0, 0
    while (math.fabs(math_value - series_value) > eps and n <= MAX_ITERS):
        series_value += 2 / (2 * n + 1) / (x ** (2 * n + 1))
        n += 1

    print('+'.join(['-' * 10, '-' * 5, '-' * 16, '-' * 16, '-' * 15]))
    print(f"{'x': ^10}|{'n': ^5}|{'series ln(1-x)': ^16}|{'math ln(1-x)': ^16}|{'eps': ^15}")
    print('+'.join(['-' * 10, '-' * 5, '-' * 16, '-' * 16, '-' * 15]))
    print(f'{x: ^10.6f}|{n: ^5}|{series_value: ^16.10f}|{math_value: ^16.10f}|{eps: ^15.10f}')
    print('-' * 66)

    if (math.fabs(math_value - series_value) > eps):
        print('Outcome error > eps!')