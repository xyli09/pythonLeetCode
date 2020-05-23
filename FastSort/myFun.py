
import random

def getMid(nList,l,r):

    tmp = nlist[r]
    while l<r:

        while l < r and nlist[l] <= tmp:
            l += 1
        nList[r] =  nList[l]
        while l < r and nlist[r] >= tmp:  # 第一步：找右边比左边tmp小的数，移动右边index
            r -= 1  # 往左走一步
        nlist[l] = nlist[r]

    nList[l] = tmp
    return l


#递归partition函数
def partition(li,left,right):
    tmp=li[left]
    while left<right:
       while left<right and li[right]>=tmp:  #第一步：找右边比左边tmp小的数，移动右边index
           right=right-1   #往左走一步
       li[left]=li[right]                    #第二步：把右边的数写到左边的位置上来
       #print(li,"right")
       while left<right and li[left]<=tmp:   #第三步：找左边比起大的数，移动左边index
            left=left+1
       li[right]=li[left]                    #第四步 左边移到右边
       #print(li,"left")
    li[left]=tmp    #把tmp归位
    return left

def QuiskSort(nList,l,r):
    if  l >= r:
        return nList

    mid = getMid(nList,l,r)
    QuiskSort(nList,l,mid -1)
    QuiskSort(nList,mid +1,r)

    return nList


nlist = list(range(200))
random.shuffle(nlist)
r = len(nlist)
res = QuiskSort(nlist,0,r-1)
print(res)


