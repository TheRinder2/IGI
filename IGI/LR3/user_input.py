def try_again_decor(func):
    def wrapper(*args, **kwargs):
        while True:
            try:
                x = func(*args, **kwargs)
                break
            except ValueError:
                print("Sorry, try again.")
        return x
    return wrapper


@try_again_decor
def user_in(msg, type_in):
    n = type_in(input(msg))
    return n
