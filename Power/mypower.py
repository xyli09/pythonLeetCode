

def Power( base, exponent):
    if exponent < 0:
        exponent = -exponent
        return 1/Power(base,exponent)
    if exponent == 2:
        return base * base
    if exponent % 2 != 0:
        exponent = exponent - 1
        return Power(base, exponent)*base
    tb = base * base
    exponent = exponent / 2
    return Power(tb, exponent)


print(Power(3,7))