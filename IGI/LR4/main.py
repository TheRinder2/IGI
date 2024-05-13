from decorators import try_again_decorator
from task2 import task2
from task1 import task1
from task3 import task3
from task4 import task4
from task5 import task5


print("""Laboratory work №4, Chopchits Dmitriy, 05.05.2024.\n""")


@try_again_decorator
def main():
    option = input('Choose task number (1-5): ')
    while not option.strip() in ['1', '2', '3', '4', '5']:
        option = input('Try again! 1-5?: ')

    match option.strip():
        case '1': 
            print(task1.__doc__)
            task1()
        case '2':
            print(task2.__doc__)
            task2()
        case '3': 
            print(task3.__doc__)
            task3()
        case '4': 
            print(task4.__doc__)
            task4()
        case '5': 
            print(task5.__doc__)
            task5()

            
if __name__ == '__main__':
    main()
