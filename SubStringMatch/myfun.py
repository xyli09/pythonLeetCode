

def match(big,aim):
    big = list(big)
    aim = list(aim)
    tt = 0
    for char in big:
        if tt == 0 :
            tmp = aim.copy()
            count = 0

        for i in range(len(tmp)):
            ta = tmp[i]
            if tmp[i] == "_":
                continue
            if char == tmp[i]:
                tmp[i] = "_"
                count += 1
                break


        if count == 0:
            tt =0
        else:
            tt += 1
            count = 0
        if tt == len(aim):
            return True

    return False

big = "thisisatest"
aim = "it"

print(match(big,aim))

