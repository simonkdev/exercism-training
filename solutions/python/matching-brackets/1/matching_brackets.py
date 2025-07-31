def is_paired(input_string):
    parentho = 0
    braceo = 0
    bracko = 0
    lastbracket = []
    lastbrace = []
    lastparenth = []
    for index, char in enumerate(input_string):
        if char == "(":
            parentho = parentho + 1
            lastparenth.append(index)
        if char == ")":
            if parentho <= 0:
                return False
            parentho = parentho - 1
            if "[" in input_string[lastparenth[-1]:index] and not "]" in input_string[lastparenth[-1]:index]:
                return False
            if "{" in input_string[lastparenth[-1]:index] and not "}" in input_string[lastparenth[-1]:index]:
                return False
            lastparenth.pop(-1)
        if char == "[":
            bracko = bracko + 1
            lastbracket.append(index)
        if char == "]":
            if bracko <= 0:
                return False
            bracko = bracko - 1
            if "(" in input_string[lastbracket[-1]:index] and not ")" in input_string[lastbracket[-1]:index]:
                return False
            if "{" in input_string[lastbracket[-1]:index] and not "}" in input_string[lastbracket[-1]:index]:
                return False
            lastbracket.pop(-1)
        if char == "{":
            braceo = braceo + 1
            lastbrace.append(index)
        if char == "}":
            if braceo <= 0:
                return False
            braceo = braceo - 1
            if "[" in input_string[lastbrace[-1]:index] and not "]" in input_string[lastbrace[-1]:index]:
                return False
            if "(" in input_string[lastbrace[-1]:index] and not ")" in input_string[lastbrace[-1]:index]:
                return False
            lastbrace.pop(-1)
    if parentho != 0 or braceo != 0 or bracko != 0:
        return False
    return True