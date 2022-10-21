# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        @cache
        def dfs(node,vis = False):
            if not node :
                return 0
            if not vis:
                m1 = dfs(node.left,False)
                m2 = dfs(node.left,True)
                m3 = dfs(node.right,False)
                m4 = dfs(node.right,True)
                return max(m1+m3,m1+m4,m2+m3,m2+m4)
            return node.val + dfs(node.left,False) + dfs(node.right, False)
        return max(dfs(root),dfs(root,True))
                
            