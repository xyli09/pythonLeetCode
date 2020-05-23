

class Solution2:
    def lengthOfLIS(self, nums: [int]) -> int:
        tails, res = [0] * len(nums), 0
        for num in nums:
            i, j = 0, res
            while i < j:
                m = (i + j) // 2
                if tails[m] < num: i = m + 1 # 如果要求非严格递增，将此行 '<' 改为 '<=' 即可。
                else: j = m
            tails[i] = num
            if j == res: res += 1
        return res,tails
inlist = [21,22,23,24,25,10, 9, 2, 5, 3, 7, 101, 18, 20]

s2 = Solution2()
# res2 = s1.testBLS(10)
# print(res2)

res3 = s2.lengthOfLIS(inlist)
print(res3)
