def answer(question):
    supported = ["minus", "plus", "multiplied", "divided"]
    operation = question[:-1].split(" ")
    operation = operation[2:]
    if len(operation) == 1 and operation[0] in "1234567890":
        return int(operation[0])
    if len(operation) == 3 and operation[1] in supported:
        if operation[1] == "minus":
            return int(operation[0]) - int(operation[2])
        if operation[1] == "plus":
            return int(operation[0]) + int(operation[2])
    if len(operation) == 4 and operation[1] in supported and operation[2] == "by":
        if operation[1] == "multiplied":
            return int(operation[0]) * int(operation[3])
        if operation[1] == "divided":
            return int(operation[0]) // int(operation[3])
    else:
        for index, item in enumerate(operation):
            if item == "by":
                operation.pop(index)
        buff = operation[1:]
        if len(operation) < 1:
            raise ValueError("syntax error")
        try:
            val = int(operation[0])
        except ValueError:
            raise ValueError("syntax error")
        if val < 0 and len(operation) == 1:
            return val
        justused = 99
        for idx, item in enumerate(buff):
            if item in supported:
                if item == "multiplied":
                    try:
                        val = val * int(buff[idx+1])
                        justused = idx+1
                    except (IndexError, ValueError):
                        raise ValueError("syntax error")
                if item == "divided":
                    try:
                        val = val // int(buff[idx+1])
                        justused = idx+1
                    except (IndexError, ValueError):
                        raise ValueError("syntax error")
                if item == "plus":
                    try: 
                        val = val + int(buff[idx+1])
                        justused = idx+1
                    except (IndexError, ValueError):
                        raise ValueError("syntax error")
                if item == "minus":
                    try:
                        val = val - int(buff[idx+1])
                        justused = idx+1
                    except (IndexError, ValueError):
                        raise ValueError("syntax error")
            if item not in supported and item.isalpha():
                raise ValueError("unknown operation")
            if item not in supported and not item.isalpha() and not idx == justused:
                raise ValueError("syntax error")
        return val