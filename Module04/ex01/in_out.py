def square(x: int | float) -> int | float:
    '''Makes a square'''
    return (x ** 2)


def pow(x: int | float) -> int | float:
    '''pow of itself'''
    return (x ** x)


def outer(x: int | float, function) -> object:
    '''outer function, go ask chatGPT for what it does'''
    count = x

    def inner() -> float:
        nonlocal count
        count = function(count)
        return count

    return inner
