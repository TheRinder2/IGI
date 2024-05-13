import builtins


def valid_type(msg: str, type_name: str) -> int:
    """Inputs desired type.
    
    Position parameters:
    msg -- input message;
    type_name -- name of the desired type."""
    
    terminate = 1
    while terminate:
        try:
            terminate = 0
            param = getattr(builtins, type_name)(input(msg))
        except ValueError as err:
            terminate = 1
            print('Value error: ', err, '\tTry again!\n')

    return param


def list(n: int) -> list:
    """Reads n elements of list from the console."""
    return input(f'Enter list with {n} elements: ').strip().split()


def validate_list(n: int, lst: list) -> bool:
    """Validates float list members.
    
    Position parameters:
    n -- desired size;
    lst -- list with floats."""

    try:
        for i in range(n):
            lst[i] = getattr(builtins, 'float')(lst[i])
    except (ValueError, IndexError):
        return False
    
    return n == len(lst)