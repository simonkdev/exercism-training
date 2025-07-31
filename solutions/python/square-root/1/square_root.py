def square_root(number):
    x = 0
    while x**2 != number:
        x = x + 1
    return x