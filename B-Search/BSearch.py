





        # write code here



class BSSolution:
    def binarySearch(self,list,l,r,n):
        if l > r :
            return -1

        mid = int(l + (r - l)/2)
        # 元素整好的中间位置
        if list[mid] == n:
            return mid
        if list[mid] < n:
            return self.binarySearch(list, mid ,r ,n)
        else:
            return self.binarySearch(list, l, mid, n)



s1 = BSSolution()
# res2 = s1.testBLS(10)
# print(res2)

res3 = s1.lenLIS()

print(res3)
