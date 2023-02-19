# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        que = deque([root])
        ans = [[root.val]]
        b = True
        while que :
            l = len(que)
            for _ in range(l):
                temp = que.popleft()
                if temp.left:
                    que.append(temp.left)
                if temp.right:
                    que.append(temp.right)
                
            if que:
                if b:
                    ans.append([i.val for i in list(reversed(que))])
                    b = False
                else:
                    ans.append([i.val for i in que])
                    b = True
        return ans
