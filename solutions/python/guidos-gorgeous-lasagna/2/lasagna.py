EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    time = EXPECTED_BAKE_TIME - elapsed_bake_time
    return time


def preparation_time_in_minutes(number_of_layers):
    """ Calculate the time for preparation required.
    :param number_of_layers: int - number of layers we want
    :constant PREPARATION_TIME: int - number of minutes required per layer
    :return: int - required time for prep

    Function takes number of layers and multiplies by time per layer, then returns as required prep time.
    """
    prep_time = PREPARATION_TIME * number_of_layers
    return prep_time

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """ Calculate elapsed time so far.
    
    :param number_of_layers: int - the number of layers in the lasagna.
    :param elapsed_bake_time: int - elapsed cooking time.
    :return: int - total time elapsed (in minutes) preparing and cooking.

    This function takes two integers representing the number of lasagna layers and the
    time already spent baking and calculates the total elapsed minutes spent cooking the
    lasagna.
    
    """
    elap_time = preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
    return elap_time