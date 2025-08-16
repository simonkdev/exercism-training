def response(hey_bob):
    if checkEmpty(hey_bob):
        return "Fine. Be that way!"
    if checkYell(hey_bob):
        return "Whoa, chill out!"
    if checkForceFullQuestion(hey_bob):
        return "Calm down, I know what I'm doing!"
    if checkQuestion(hey_bob):
        return "Sure."
    return "Whatever."
    
def checkEmpty(msg):
    msg = msg.strip()
    if msg == "":
        return True
    return False

def checkYell(msg):
    msg = msg.strip()
    if msg.isupper() and not msg.endswith('?'):
        return True
    return False

def checkQuestion(msg):
    msg = msg.strip()
    if msg.endswith('?'):
        return True
    return False

def checkForceFullQuestion(msg):
    msg = msg.strip()
    if msg.isupper() and msg.endswith('?'):
        return True
    return False