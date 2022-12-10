# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        dp = {}
        def dfs(node):
            if not node:
                return 0
            dp[node] = node.val + dfs(node.left) + dfs(node.right) 
            return dp[node]
        tot = dfs(root)
        ans = -float('inf')
        stk = [root]
        while stk:
            temp = stk.pop()
            ans = max(dp[temp]*(tot - dp[temp]),ans)
            if temp.left:
                stk.append(temp.left)
            if temp.right:
                stk.append(temp.right)
        return ans %(10**9 + 7)
                