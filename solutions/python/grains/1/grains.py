def square(number):
    if number <= 64 and number >=1:
        buffer = 1
        for x in range(1, number):
            buffer = buffer * 2
        return buffer
    raise ValueError("square must be between 1 and 64")


def total():
    buffer = 1
    result = 0
    for x in range(0, 64):
        result = result + square(buffer)
        buffer = buffer + 1
    return result
