# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        stk = [root]
        mm = min(p.val, q.val)
        mx = max(p.val, q.val)
        
        while stk:
            temp = stk.pop()
            if temp.val <= mx and temp.val >= mm:
                return temp
            if temp.left:
                stk.append(temp.left)
            if temp.right:
                stk.append(temp.right)
                