def score(x, y):
    idx = x*x + y*y
    if idx > 100:
        return 0
    if idx <= 100 and idx > 25:
        return 1
    if idx <= 25 and idx > 1:
        return 5
    if idx <=1:
        return 10