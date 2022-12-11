# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = {}
        def dfs(node):
            if not node:
                return 0
            temp =max(0, max(node.val+dfs(node.left),node.val+dfs(node.right)))
            ans[node] = temp
            return temp
        dfs(root)
        res = -float('inf')
        stk = [root]
        while stk:
            temp = stk.pop()
            value = temp.val
            if temp.left :
                stk.append(temp.left)
                value += ans[temp.left]
            if temp.right :
                stk.append(temp.right)
                value += ans[temp.right]
            res = max(res,value)
        return res
                
            
            