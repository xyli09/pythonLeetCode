

class Solution:
    def FindContinuousSequence(self, tsum):
        list = [i for i in range(1,tsum)]
        left,right = 0,0

        while right < tsum:

            sum = 0
            for i in range(left,right):
                sum += list[i]
            if sum == tsum:
                print(left, "\t", right)
            if sum < tsum:
                right += 1
            else :
                left += 1
                right = left + 1

s = Solution()
s.FindContinuousSequence(100)
# write code here
