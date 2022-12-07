# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        ans = 0
        stk = [root]
        while stk:
            temp = stk.pop()
            if low <= temp.val <= high:
                ans += temp.val
            if temp.left:
                stk.append(temp.left)
            if temp.right:
                stk.append(temp.right)
        return ans
                