# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        que = deque([[root, 1]])
        ans = 0
        
        while que:
            r = len(que)
            ans = max(ans, que[-1][1] - que[0][1] + 1)
            for _ in range(r):
                temp, pos = que.popleft()
                
                if temp.left:
                    que.append([temp.left, pos*2])
                if temp.right:
                    que.append([temp.right, (pos*2)+1])
                    
        return ans
            