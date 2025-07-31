def is_armstrong_number(number):
    digits = []
    sum = 0
    for digit in str(number):
        digits.append(int(digit))
    for digit in digits:
        product = 1
        for y in range(0, len(digits)):
            product = product * digit
        sum = sum + product
    if sum == number:
        return True
    return False