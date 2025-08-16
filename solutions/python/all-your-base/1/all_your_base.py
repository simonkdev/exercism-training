def rebase(input_base, digits, output_base):
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    if output_base < 2:
        raise ValueError("output base must be >= 2")
    if sum(digits) == 0:
        return [0]
    value = 0
    tmp = 0
    for x in range(0, len(digits)):
        if digits[x] < 0 or digits[x] >= input_base:
            raise ValueError("all digits must satisfy 0 <= d < input base")
        value = value + (digits[x] * input_base**(len(digits) - tmp - 1))
        tmp = tmp + 1
    tmp = value
    out = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    i = 1
    while tmp != 0 and i <= len(out):
        remainder = tmp % output_base
        out[-i] = remainder
        tmp = tmp // output_base
        i = i + 1
    while out[0] == 0:
        out.pop(0)
    return out