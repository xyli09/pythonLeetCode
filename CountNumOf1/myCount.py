

def NumberOf1( n):
    count = 0
    if n < 0:
        n= n&0xffffffff
    while n:
        t = bin(n)
        print(t)
        n = n & (n - 1)
        count =count+1
    return count


print(NumberOf1(-1))