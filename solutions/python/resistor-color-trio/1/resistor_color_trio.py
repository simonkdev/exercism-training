def label(colors):
    cols = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
    val = 0
    val = val + cols.index(colors[0]) * 10
    val = val + cols.index(colors[1])
    val = val * 10**cols.index(colors[2])
    if val >= 1000 and val < 1000000:
        return str(val // 1000) + " kiloohms"
    elif val >= 1000000 and val < 1000000000:
        return str(val // 1000000) + " megaohms"
    elif val >= 1000000000:
        return str(val // 1000000000) + " gigaohms"        
    return str(val) + " ohms"
