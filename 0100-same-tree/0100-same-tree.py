# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(node,vals,isleft = True):
            if not node:
                return
            dfs(node.left,vals,True)
            vals.append((node.val,isleft))
            dfs(node.right,vals,False)
            
        one = []
        two = []
        dfs(q,one)
        dfs(p,two)
        return one == two