import math
from math import *
from prettytable import PrettyTable
from user_input import user_in


def task1() -> PrettyTable:
    """
    Calculate ln(x+1/x-1) by series
    Arg: x, eps
    |X| > 1
    :return: table with answers
    """

    N = 500
    while True:
        try:
            x = user_in("Enter X:\n", float)
            assert abs(x) > 1
            break
        except AssertionError:
            print("We need |x| > 1!")

    eps = user_in("Enter eps:\n", float)

    mathf = (log((x + 1) / (x - 1)))

    sum_f = 0
    n = 0
    while abs(sum_f - mathf) > eps and n < N:
        sum_f += 2 * (1 / ((2*n + 1) * x ** (2 * n + 1)))
        n += 1

    th = ["X", "N", "F(x)", "Math F(x)", "eps"]
    td = [str(x), str(n), str(sum_f), str(mathf), str(eps)]

    columns = len(th)

    table = PrettyTable(th)

    td_data = td[:]
    while td_data:
        table.add_row(td_data[:columns])
        td_data = td_data[columns:]

    return table
