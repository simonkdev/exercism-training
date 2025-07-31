def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")

    sum = 0
    for x in aliquots(number):
        sum = sum + x
    if sum == number:
        return "perfect"
    if sum > number:
        return "abundant"
    if sum < number:
        return "deficient"
        

def aliquots(num):
    aliquots = []
    for x in range(1, num - 1):
        if num % x == 0:
            aliquots.append(x)
    return aliquots
