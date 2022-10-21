# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    @cache
    def dfs(self,node,vis = False):
        if not node :
            return 0
        if not vis:
            move1 = self.dfs(node.left)
            move2 = self.dfs(node.left,True)
            move3 = self.dfs(node.right)
            move4 = self.dfs(node.right,True)
            return max(move1+move3,move1+move4,move2+move3,move2+move4)
        return node.val + self.dfs(node.left) + self.dfs(node.right)
    def rob(self, root: Optional[TreeNode]) -> int:
        return max(self.dfs(root),self.dfs(root,True))
                
            