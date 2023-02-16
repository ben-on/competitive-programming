# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        qu=deque([root])
        res=1
        while qu:
            r=len(qu)
            for i in range(r):
                temp=qu.popleft()
                if temp.left:
                    qu.append(temp.left)
                if temp.right:
                    qu.append(temp.right)
            if qu:
                res+=1
        return res
                