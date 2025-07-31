def rotate(text, key):
    chars = list(text)
    rot = key
    fin = 0
    lowerletters = "abcdefghijklmnopqrstuvwxyz"
    capletters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for x in range(0, len(chars)):
        if chars[x] in lowerletters:
            loc = lowerletters.find(chars[x])
            if loc + rot >= 26:
                fin = loc + rot - 26
            else:
                fin = loc+rot
            chars[x] = lowerletters[fin]
        elif chars[x] in capletters:
            loc = capletters.find(chars[x])
            if loc + rot >= 26:
                fin = loc + rot - 26
            else:
                fin = loc+rot
            chars[x] = capletters[fin]
    ret = "".join(chars)
    return ret