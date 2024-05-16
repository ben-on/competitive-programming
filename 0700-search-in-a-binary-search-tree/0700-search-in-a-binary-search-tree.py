# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        stk = [root]
        
        while stk:
            temp = stk.pop()
            if temp.val == val:
                return temp
            if temp.left:
                stk.append(temp.left)
            if temp.right:
                stk.append(temp.right)
                
        return None