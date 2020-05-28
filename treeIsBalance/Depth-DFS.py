

class Depth:
    def Depth_DFS(self,root):
        if root is None:
            return 0

        dl = self.DFS(root.left) + 1
        dr = self.DFS(root.right) + 1
        if dl >= dr:
            return dl
        else:
            return dr
    def Balance_DFS(self,root):
        if root is None:
            return True
        dl = self.Depth_DFS( root.left) + 1
        dr = self.Depth_DFS( root.right) + 1
        if abs(dl - dr) > 1 :
            return False
        else:
            return self.Balance_DFS(root.left) and self.Balance_DFS(root.right)