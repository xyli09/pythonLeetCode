

def mypow(n,m):
    if m < 0:
        return 1/mypow(n,-m)
    if m == 0:
        return 1
    if m == 1:
        return n
    if m % 2 == 0:
        b = int(m/2)
        res = mypow(n,b)
        return res * res
    else:
        b = (m-1)/2
        res = mypow(n, b)
        return res * res * n


print(mypow(3,-7))