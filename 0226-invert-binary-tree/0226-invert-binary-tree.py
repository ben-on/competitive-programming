# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        stk=[root]
        while stk:
            temp=stk.pop()
            temp.left,temp.right = temp.right,temp.left
            if temp.left:
                stk.append(temp.left)
            if temp.right:
                stk.append(temp.right)
        return root