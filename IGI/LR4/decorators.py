def try_again_decorator(func):
    """Allows to re-execute a parameter function."""
    def wrapper(*args, **kwargs):
        try_again = 1
        while try_again:
            func(*args, **kwargs)
            again = ""
            while again not in ['Y', 'N']:
                again = input('Call this function again (Y/N)?\n')

            try_again = again == 'Y'

    wrapper.__doc__ = func.__doc__
    
    return wrapper
