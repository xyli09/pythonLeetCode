
import random

def Myerge(lList,rList):
    r,l = 0,0
    res =[]
    if lList is None or len(lList) < 1:
        return rList
    if rList is [] or len(rList) < 1:
        return lList
    while r < len(rList) and l < len(lList):
        if lList[l] < rList[r]:
            res.append(lList[l])
            l += 1
        else:
            res.append(rList[r])
            r += 1

    if r == len(rList):
        for v in lList[l:]:
            res.append(v)
    else:
        for v in rList[r:]:
            res.append(v)
    return res

def merge(a, b):
    c = []
    h = j = 0
    while j < len(a) and h < len(b):
        if a[j] < b[h]:
            c.append(a[j])
            j += 1
        else:
            c.append(b[h])
            h += 1

    if j == len(a):
        for i in b[h:]:
            c.append(i)
    else:
        for i in a[j:]:
            c.append(i)

    return c



def DivideSort(nList):
    l = len(nList)
    if  l <= 1:
        return nList

    mid = int(l/2)

    rList = DivideSort(nList[0:mid])
    lList = DivideSort(nList[mid:])
    res = Myerge(rList,lList)
    return res


nlist = list(range(200))
random.shuffle(nlist)
r = len(nlist)
a = [4, 7, 8, 3, 5, 9]
res = DivideSort(nlist)
print(res)
