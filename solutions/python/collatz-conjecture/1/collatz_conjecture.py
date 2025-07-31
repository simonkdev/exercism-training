def steps(number):
    """
    returns the steps needed to reach 1 from the parameter number according to the Collatz Conjecture
    """
    if number < 1:
        raise ValueError("Only positive integers are allowed")
    counter = 0
    while int(number) != 1:
        if number % 2 == 0:
            number = number // 2
        else:
            number = (number * 3) + 1
        counter = counter + 1
    return counter
            
