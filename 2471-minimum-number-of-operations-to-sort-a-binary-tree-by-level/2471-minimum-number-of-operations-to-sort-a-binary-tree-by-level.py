# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        que = deque([root])
        ans = 0
        while que:
            arr = list(map(lambda x:x.val, que))
            temp_queue = que.copy()
            arr.sort()
            r = len(que)
            index = dict(zip(arr, range(r)))
            for i in range(r):
                node = temp_queue[i]
                
                while index[node.val] != i:
                    ans += 1
                    temp_queue[index[node.val]], temp_queue[i] = temp_queue[i], temp_queue[index[node.val]]
                    node = temp_queue[i]
            # print(ans, index, arr)
            for _ in range(r):
                temp = que.popleft()
                if temp.left:
                    que.append(temp.left)
                if temp.right:
                    que.append(temp.right)
            
        return ans
            