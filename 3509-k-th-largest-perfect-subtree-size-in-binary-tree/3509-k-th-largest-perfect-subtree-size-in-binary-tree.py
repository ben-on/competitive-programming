# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check(self,root):
        q = deque([root])
        ans = 0
        l = 0
        while q:
            r = len(q)
            if 2 ** l != r:
                return -1
            for i in range(r):
                temp = q.popleft()
                ans += 1
                if temp.left:
                    q.append(temp.left)
                if temp.right:
                    q.append(temp.right)
            l += 1
        
        return ans

                

    def kthLargestPerfectSubtree(self, root: Optional[TreeNode], k: int) -> int:
        hp = []

        stk = [root]

        while stk:
            temp = stk.pop()
            vv = self.check(temp)
            if vv != -1:
                hp.append(vv)
            if temp.left:
                stk.append(temp.left)
            if temp.right:
                stk.append(temp.right)
        
        hp.sort(reverse = True)

        # print(hp)
        if k <= len(hp):
            return hp[k - 1]
        
        return -1
        
            
            



        