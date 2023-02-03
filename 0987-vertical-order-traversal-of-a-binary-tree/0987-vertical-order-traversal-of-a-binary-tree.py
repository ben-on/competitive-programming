# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        res0,qu = defaultdict(list),[ (root, 0, 0) ]
        while qu:
            node, pos, depth = qu.pop(0)
            if not node: continue
            res0[(pos,depth)].append(node.val)
            res0[(pos,depth)].sort()
            qu.extend( [ (node.left, pos-1, depth+1), (node.right, pos+1, depth+1) ] )
            
            
        res = defaultdict(list)
        keys = sorted(list(res0.keys()), key=lambda x: (x[0], x[1]))
        for k in keys:
            pos, depth = k
            res[pos].extend(res0[k])
        return res.values()   