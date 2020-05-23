

def greedy(nlist):
    fit = 0
    pre = 0
    i = 0
    for n in nlist:
        if i == 0:
            pre = n
            i += 1
            continue
        i += 1
        if n > pre:
            dt = n-pre
            fit += dt
            pre = n
        else:
            pre = n
    return fit







nList = [7, 1,5,3,6,4]
nList2 = [1,2,3,4,5]
nList3 = [7,6,3,2]
res = greedy(nList2)
print(res)