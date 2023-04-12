# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        graph = defaultdict(set)
        all = set()
        hasParent = set()
        for p, c, isLeft in descriptions:
            graph[p].add((c, isLeft))
            all.add(p)
            all.add(c)
            hasParent.add(c)
        
        root = None
        
        for node in all:
            if node not in hasParent:
                root = TreeNode(node)
                break
        
        
        def dfs(parent):
            for c, isLeft in graph[parent.val]:
                if isLeft:
                    parent.left = TreeNode(c)
                    dfs(parent.left)
                else:
                    parent.right = TreeNode(c)
                    dfs(parent.right)
        
        dfs(root)
        return root
                
        
        
            