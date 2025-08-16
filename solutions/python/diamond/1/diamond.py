def rows(letter):
    alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    if letter not in alphabet:
        raise ValueError(f"Invalid letter: {letter!r}")
    
    idx  = alphabet.index(letter)      # A→0, B→1, C→2, …
    size = idx * 2 + 1                 # 1, 3, 5, 7, …

    result = []
    # Top row: centered 'A'
    pad = idx                         # same as (size-1)//2
    result.append(" " * pad + "A" + " " * pad)

    # Inner rows
    for i in range(1, size - 1):
        # Determine which letter and how much padding
        if i <= idx:
            k = i
        else:
            k = (size - 1) - i
        side_pad   = idx - k
        mid_pad    = 2 * k - 1
        letter_chr = alphabet[k]

        row = (
            " " * side_pad +
            letter_chr +
            " " * mid_pad +
            letter_chr +
            " " * side_pad
        )
        result.append(row)

    # Bottom row = same as top
    if size > 1:
        result.append(result[0])
    return result

# Quick manual test
    # Expected output for "C":
    # '  A  '
    # ' B B '
    # 'C   C'
    # ' B B '
    # '  A  '