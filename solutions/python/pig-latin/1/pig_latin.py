def translate(text):
    words = text.split()
    y = 0
    current = ""
    ret = ""
    for x in range(0, len(words)):
        current = words[x]
        if x > 0:
            ret = ret + " " + modify(current)
        else:
            ret = ret + modify(current)
    return ret

def modify(word):
    if ruleOneCheck(word):
        return ruleOneMod(word)
    if ruleThreeCheck(word):
        return ruleThreeMod(word)
    if ruleFourCheck(word):
        return ruleFourMod(word)
    if ruleTwoCheck(word):
        return ruleTwoMod(word)

def ruleOneCheck(word):
    vowels = "aeiou"
    firstChar = word[0]
    hasVowels = any(c in vowels for c in firstChar)
    if word.startswith("xr") or word.startswith("yt") or hasVowels:
        return True
    return False

def ruleOneMod(word):
    mod = word + "ay"
    return mod

def ruleTwoCheck(word):
    firstChar = word[0]
    consonants = "bcdfghjklmnpqrstvwxyz"
    startsCons = any(c in consonants for c in firstChar)
    if startsCons:
        return True
    return False

def ruleTwoMod(word):
    idx = getConsIdx(word)
    prefix = word[:idx]
    suffix = word[idx:]
    mod = suffix + prefix + "ay"
    return mod

def getConsIdx(word):
    consonants = "bcdfghjklmnpqrstvwxyz"
    vowels = "aeiou"
    idx = 0
    idxDone = False
    for x in range(0, len(word)):
        chara = word[x]
        if any(c in consonants for c in chara) and not idxDone:
            idx = idx +1
        if any(c in vowels for c in chara):
            idxDone = True            
    return idx

def ruleThreeCheck(word):
    ind = word.find("qu")
    if ind >= 0:
        for x in range(0,ind):
            vowels = "aeiou"
            if any(c in vowels for c in word[x]):
                return False
        return True
    return False

def ruleThreeMod(word):
    idx = word.find("qu")
    prefix = word[:idx+2]
    suffix = word[idx+2:]
    ret = suffix + prefix + "ay"
    return ret

def ruleFourCheck(word):
    idx = word.find("y")
    vowels = "aeiou"
    if idx > 0:
        for x in range(0,idx):
            if any(c in vowels for c in word[x]):
                return False
        return True
    return False

def ruleFourMod(word):
    idx = word.find("y")
    prefix = word[:idx]
    suffix = word[idx:]
    ret = suffix + prefix + "ay"
    return ret