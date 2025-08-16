def equilateral(sides):
    if is_triangle(sides):
        if sides[1] == sides[2] and sides[0] == sides[1]:
            return True
        return False
    return False
        


def isosceles(sides):
    if is_triangle(sides):
        if sides[0] == sides[1] or sides[0] == sides[2] or sides[1] == sides[2]:
            return True
        return False
    return False


def scalene(sides):
    if is_triangle(sides):
        if sides[1] != sides[0] and sides[1] != sides[2] and sides[0] != sides[2]:
            return True
        return False
    return False

def is_triangle(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    if a + b >= c and b + c >= a and a + c >= b:
        if a > 0 and b > 0 and c > 0:
            return True
    return False
    
