# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        ans = 0
        
        def dfs(head):
            nonlocal ans
            if not head:
                return (float('inf'), -float('inf'))
            mml, mxl = dfs(head.left)
            mmr, mxr = dfs(head.right)
            
            mx = max(head.val, max(mxl, mxr))
            mm = min(head.val, min(mml, mmr))
            
            # calc the answer
            val1 = abs(head.val - mm)
            val2 = abs(head.val - mx)
            ans = max(ans, max(val1, val2))
            
            return (mm, mx)
        
        dfs(root)
        return ans
            
                