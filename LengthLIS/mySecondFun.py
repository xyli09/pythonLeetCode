

#  二分查找
class LISSolution:
    def lenLIS(self):
        # inlist = [10,9, 2, 5, 3, 7, 101, 18, 20]
        inlist = [21,22,23,24,25,10, 9, 2, 5, 3, 7, 101, 18, 20]
        return self.GetLIS(inlist)


    def GetLIS(self,list ):
        res = []
        for v in list:
            pos = self.binaryLowSearch(res,0,len(res)-1,v)
            if len(res) <= pos or pos == -1 :
                res.append(v)
            else:
                res[pos] = v
        return res
    def testBLS(self,n):
        testList = [1,2,3,4,5,6,8,9]
        return self.binaryLowSearch(testList,0,len(testList)-1,n)

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