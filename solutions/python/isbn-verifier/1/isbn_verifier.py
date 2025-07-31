def is_valid(isbn):
    tmp = isbn.split("-")
    tmp = "".join(tmp)
    isbn = tmp
    if len(isbn) != 10:
        return False
    digits = []
    chars = "ABCDEFGHIJKLMNOPQRSTUVWYZabcdefghijklmnopqrstuvwyz"
    for x in range(0, len(isbn) - 1):
        if isbn[x] in chars or isbn[x] in "Xx":
            return False
        digits.append(int(isbn[x]))
    if isbn[-1] == "X":
        digits.append(10)
    elif isbn[-1] in chars:
        return False
    else:
        digits.append(int(isbn[-1]))
    factor = 10
    sum = 0
    for x in digits:
        sum = factor*x + sum
        factor = factor - 1
    if sum % 11 == 0:
        return True
    return False