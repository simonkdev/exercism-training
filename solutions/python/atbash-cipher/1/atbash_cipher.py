def encode(plain_text):
    plain = list("abcdefghijklmnopqrstuvwxyz")
    cipher = list("zyxwvutsrqponmlkjihgfedcba")
    code = []
    counter = 0
    plain_text = plain_text.lower()
    for char in plain_text:
        if counter == 5:
            code.append(" ")
            counter = 0
        if char in " .,:!?":
            continue
        if char in "1234567890":
            code.append(char)
        else:
            code.append(cipher[plain.index(char)])
        counter = counter + 1
    code = "".join(code)
    return code.strip()
    
def decode(ciphered_text):
    plain = list("abcdefghijklmnopqrstuvwxyz")
    cipher = list("zyxwvutsrqponmlkjihgfedcba")
    code = []
    ciphered_text = ciphered_text.lower()
    for char in ciphered_text:
        if char in " .,:!?":
            continue
        if char in "1234567890":
            code.append(char)
        else:
            code.append(cipher[plain.index(char)])
    code = "".join(code)
    return code.strip()
    