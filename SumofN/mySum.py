



def sol(n,m):
    if n== 1 or m ==1:
        return 1
    elif n == m and n > 1:
        return sol(n,n-1)+1
    elif n < m:
        return sol(n,n)
    elif n > m:
        return sol(n,m-1)+sol(n-m,m)
    return 0

n = 9
m = 5
print(sol(9,5))