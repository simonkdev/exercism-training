"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 4


def sublist(list_one, list_two):
    if is_sublist(list_one, list_two):
        return SUBLIST
    if is_superlist(list_one, list_two):
        return SUPERLIST
    elif list_one == list_two:
        return EQUAL
    return UNEQUAL

def is_sublist(list1, list2):
    if len(list1) > len(list2):
        return False
    if list1 == [] and list2 != []:
        return True
    elif list1 == list2:
        return False
    for i in range(len(list2) - len(list1) + 1):
        if list2[i:i + len(list1)] == list1:
            return True
    return False

def is_superlist(list1, list2):
    return is_sublist(list2, list1)
