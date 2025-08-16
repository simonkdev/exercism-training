def is_pangram(sentence):
    low = sentence.lower()
    letters = "abcdefghijklmnopqrstuvwxyz"
    ind = 0
    for x in range(0, len(letters)):
        if letters[x] in low:
            ind = ind + 1
    if ind == len(letters):
        return True
    return False