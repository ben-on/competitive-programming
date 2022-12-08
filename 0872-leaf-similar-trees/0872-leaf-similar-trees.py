# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        one = []
        two = []
        stk = [root1]
        while stk:
            temp = stk.pop()
            if not temp.left and not temp.right:
                one.append(temp.val)
            if temp.left:
                stk.append(temp.left)
            if temp.right:
                stk.append(temp.right)
        stk = [root2]
        while stk:
            temp = stk.pop()
            if not temp.left and not temp.right:
                two.append(temp.val)
            if temp.left:
                stk.append(temp.left)
            if temp.right:
                stk.append(temp.right)
        return one == two
        