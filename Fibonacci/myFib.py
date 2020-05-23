
class Solution:
    def Fibonacci(self, n):
        if n == 1:
            return 1
        if n == 2:
            return 2
        sum = [0 for i in range(n+1)]
        print(sum)
        sum[0]=0
        sum[1]=1
        sum[2]=2

        for i in range(3,n+1):
                 sum[i]=  sum[i-1]+sum[i-2]
            # res =0
        # for i in sum :


        return sum[n]
        # write code here