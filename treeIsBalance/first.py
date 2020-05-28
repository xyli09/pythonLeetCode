

class TreeNode():
    def __init__(self,x):
        self.val  = x
        self.left = None
        self.right = None


class Solution:
    def getDeepth(self,Root):
        if Root is None:
            return 0
        nright = self.getDeepth(Root.right)
        nleft = self.getDeepth(Root.left)
        return max(nright,nleft)+1
    def IsBalance_solution(self,pRoot):
        if pRoot is None:
            return True
        right = self.getDeepth(pRoot.right)
        left = self.getDeepth(pRoot.left)
        if abs(right - left) > 1:
            return False
        return self.IsBalance_solution(pRoot.right) and self.IsBalance_solution(pRoot.left)