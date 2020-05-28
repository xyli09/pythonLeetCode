

#  二分查找
class LISSolution:

# 思路：维护一个序列（不是最终的上升序列,但是序列的长度跟上升子序列长度一致）。当前元素与最后一个元素比较，大于则添加到序列，小于则替换掉最后的元素
    def GetLIS(self,list ):
        res = [list[0]]
        for v in list:
            # pos = self.binaryLowSearch(res,0,len(res)-1,v)
            pos = self.makeIncreaseList(res, v)
            print(v,"\t",pos,"\t",res)
            if len(res) <= pos or pos == -1 :
                res.append(v)
            else:
                res[pos] = v
        return res

    def testBLS(self,n):
        testList = [1,3,4,5,6,8,9]
        return self.binaryLowSearch(testList,0,len(testList)-1,n)

    # 二分查找
    def binaryLowSearch(self,list,l,r,n):
        if l > r :
            return -1

        if n > list[r] :
            return r + 1
        if n < list[l]:
            return l
        mid = int(l + (r - l)/2)
        if list[mid] == n :
            return mid
        if list[mid] < n and list[mid +1] > n:
            return mid + 1
        if list[mid] < n :
            return self.binaryLowSearch(list,mid,r,n)
        else:
            return self.binaryLowSearch(list,l,mid,n)

    #普通查找
    def makeIncreaseList(self,list,n):
        index = 0
        if n <= list[0]:
            return 0
        for i in range(1,len(list)):

            if list[i-1] < n <= list[i] :
                return i
        return -1


# inlist = [10,9, 2, 5, 3, 7, 101, 18, 20]
inlist = [21,22,23,24,25,10, 9, 2, 5, 3, 7,101, 18, 20]
s = LISSolution()

result = s.GetLIS(inlist)

print(result)

# print(s.testBLS(2))