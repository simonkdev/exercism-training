def is_isogram(string):
    string = string.lower()
    letters = list(string)
    english = "abcdefghijklmnopqrstuvwxyz"
    for idx in range(0, len(letters)):
        char = letters[idx]
        letters[idx] = ""
        if char in letters and char in english:
            return False
    return True