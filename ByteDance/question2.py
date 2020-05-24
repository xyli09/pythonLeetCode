


def question1():
    str = input("请输入:").split()
    n = int(str[0],10)
    m = int(str[1],10)
    c = int(str[2],10)
    clist = [[0 for j in range(n)] for i in range(c)]
    # printMatrix(clist)
    #c1 1 2 3 4 5
    #c2
    for i in range(n):
        strlist = input("input color:").split()
        num = int(strlist[0], 10)
        if num == 0:
            continue
        j = 0
        for str in strlist:
            if j== 0:
                j += 1
                continue
            j += 1
            jc = int(str,10)
            clist[jc-1][i] = 1
    # printMatrix(clist)
    return getCount(clist,m)


def printMatrix(clist):
    for i in clist:
        print(i)

def getCount(nlist,m):
    count = 0
    for k in nlist:
        count += getRow(k,m)
    return count

def getRow(nlist,m):
    tlist = nlist[:m]
    nlist.extend(tlist)
    # print(nlist)
    ill = 0
    count = 0
    for i in range(len(nlist) - m):
        if i == 0:
            t = nlist[i:i+m]
            # print(t)
            count = getSum(t)
        else:
            # print("a:",i-1,"b:",i+m -1)
            count = count - nlist[i-1] + nlist[i + m -1 ]
        # print("count:",count)
        if count > 1:
            ill += 1
            break
    return ill

def getSum(nlist):
    res = 0
    for i in nlist:
        if i== 0:
            continue
        res += i
    return res

print(question1())
