from user_input import user_in


def task2() -> float:
    """
    Calculate the average sum of all your even numbers! Until 1.
    :return: Average sum
    """
    x = 0
    i = 1
    sum2 = 0
    cnt2 = 0
    while x != 1:
        x = user_in(f"Enter {i}th number\n", int)

        sum2 += x if x % 2 == 0 else 0
        cnt2 += 1 if x % 2 == 0 else 0
        i += 1

    return (sum2 / cnt2) if cnt2 > 0 else 0
