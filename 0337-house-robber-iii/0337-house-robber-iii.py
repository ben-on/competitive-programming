# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    dp = {}
    def dfs(self,node,vis = False):
        if not node :
            return 0
        if (node,vis) in self.dp:
            return self.dp[(node,vis)]
        if not vis:
            move1 = self.dfs(node.left,False)
            move2 = self.dfs(node.left,True)
            move3 = self.dfs(node.right,False)
            move4 = self.dfs(node.right,True)
            self.dp[(node,vis)] = max(move1+move3,move1+move4,move2+move3,move2+move4)
        else:
            self.dp[(node,vis)] = node.val + self.dfs(node.left,False) + self.dfs(node.right, False)
        return self.dp[(node,vis)]
    def rob(self, root: Optional[TreeNode]) -> int:
        return max(self.dfs(root),self.dfs(root,True))
                
            