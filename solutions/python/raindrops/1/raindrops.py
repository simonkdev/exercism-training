import math

def convert(number):
    conv = checkPling(number) + checkPlang(number) + checkPlong(number)
    if conv == "":
        return str(number)
    return conv

def checkPlong(number):
    if(number % 7 == 0):
        return "Plong"
    return ""

def checkPlang(number):
    if(number % 5 == 0):
        return "Plang"
    return ""

def checkPling(number):
    if(number % 3 == 0):
        return "Pling"
    return ""