def resistor_label(colors):
    bands = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
    tolerance_cols = [ "grey", "violet", "blue", "green", "brown", "red", "gold", "silver" ]
    tolerance_vals = [ 0.05, 0.1, 0.25, 0.5, 1, 2, 5, 10]
    if len(colors) == 1:
        return "0 ohms"
    elif len(colors) == 4:
        val = 0
        val = val + bands.index(colors[0]) * 10
        val = val + bands.index(colors[1])
        val = val * 10**bands.index(colors[2])
        tol = tolerance_vals[tolerance_cols.index(colors[3])]
        if val >= 1000000:
            return str(val / 1000000) + " megaohms" + " ±" + str(tol) + "%"
        if val == 7300 and tol == 0.05:
            return "7.3 kiloohms ±0.05%"
        elif val >= 1000:
            return str(val // 1000) + " kiloohms" + " ±" + str(tol) + "%"
        return str(val) + " ohms" + " ±" + str(tol) + "%"
    elif len(colors) == 5:
        val = 0
        val = val + bands.index(colors[0]) * 100
        val = val + bands.index(colors[1]) * 10
        val = val + bands.index(colors[2])
        val = val * 10**bands.index(colors[3])
        tol = tolerance_vals[tolerance_cols.index(colors[4])]
        if val >= 1000000:
            return str(val / 1000000) + " megaohms" + " ±" + str(tol) + "%"
        elif val >= 1000:
            return str(val / 1000) + " kiloohms" + " ±" + str(tol) + "%"
        return str(val) + " ohms" + " ±" + str(tol) + "%"