

def onceBuySell(nlist):
    fit = 0
    min = 0
    maxProfit = 0
    i = 0
    for n in nlist:
        if i == 0:
            min = n
            i += 1
            continue
        i += 1
        if n > min:
            dt = n-min
            if dt > maxProfit:
                maxProfit = dt
        else:
            min = n
    return maxProfit







nList = [7, 1,5,3,6,4]
nList2 = [1,2,3,4,5]
nList3 = [7,6,3,2]
res = onceBuySell(nList3)
print(res)