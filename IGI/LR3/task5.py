from functools import reduce
from generator import generator
from user_input import user_in


def task5():
    """
    a) Sum all negative numbers of array
    b) Print numbers between min_element and max_element
    c) Multiple numbers between min_element and max_element
    """
    option = ""
    while option not in ["1", "2"]:
        print("Enter 1 to generate array, 2 to enter array\n")
        option = input("Enter: ")

    if option == "1":
        n = user_in("Enter n (size of array): ", int)
        array = [i for i in generator(n)]
    else:
        while True:
            try:
                array = list(map(float, input("Enter string of numbers splited by space.\n").split()))
                break
            except ValueError:
                print("Sorry, try again")
    print("array:\n", array)

    max_idx = max(enumerate(array), key=lambda x: x[1])[0]
    min_idx = min(enumerate(array), key=lambda x: x[1])[0]

    print("Index of min element:", min_idx, "\nIndex of max element:", max_idx)

    n_sum = sum([i for i in array if i < 0])
    print("Sum of negative numbers:", n_sum)

    print("Array between min and max elements: \n", array[min(min_idx, max_idx)+1:max(min_idx, max_idx)])

    if array[min(min_idx, max_idx)+1:max(min_idx, max_idx)]:
        mult = reduce(lambda x, y: x * y, array[min(min_idx, max_idx)+1:max(min_idx, max_idx)])
    else:
        mult = "Not numbers here."
    print(mult)



