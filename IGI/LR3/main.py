from task1 import task1
from task2 import task2
from task3 import task3
from task4 import task4
from task5 import task5


if __name__ == '__main__':

    print("Laboratory work #3, Dmitriy Chopchits, 01.04.2024")

    param = ""
    while param != "exit":
        while param not in ["1", "2", "3", "4", "5", "exit"]:
            param = input("Enter number(1-5) or exit to close.\n").strip()

        match param:
            case "1":
                print(task1.__doc__.strip("\n"))
                print(task1())
            case "2":
                print(task2.__doc__.strip("\n"))
                print(task2())
            case "3":
                print(task3.__doc__.strip("\n"))
                print(task3())
            case "4":
                print(task4.__doc__.strip("\n"))
                print(task4())
            case "5":
                print(task5.__doc__.strip("\n"))
                task5()
            case "exit":
                break
        param = ""

