def value(colors):
    cols = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
    val = 0
    val = val + cols.index(colors[0]) * 10
    val = val + cols.index(colors[1])
    return val
