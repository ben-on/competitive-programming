# illegal

class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0
        self.max_l = 0  

class Solution:
    def longestCommonPrefix(self, words: List[str], k: int) -> List[int]:
        root = TrieNode()
        
        for word in words:
            node = root
            node.count += 1
            for c in word:
                if c not in node.children:
                    node.children[c] = TrieNode()
                node = node.children[c]
                node.count += 1
        
        def compute_max_l(node, current_depth):
            max_l = 0
            if node.count >= k:
                max_l = current_depth
            for child in node.children.values():
                child_max = compute_max_l(child, current_depth + 1)
                if child_max > max_l:
                    max_l = child_max
            node.max_l = max_l
            return max_l
        
        compute_max_l(root, 0)
        
        answers = []
        
        for i in range(len(words)):
            word = words[i]
            path = []
            node = root
            depth = 0
            path.append((node, depth))
            for c in word:
                if c not in node.children:
                    break
                node = node.children[c]
                depth += 1
                path.append((node, depth))
            
            root.count -= 1
            for (n, d) in path[1:]:
                n.count -= 1
            
            for (n, d) in reversed(path):
                new_max = 0
                if n.count >= k:
                    new_max = d
                for child in n.children.values():
                    if child.max_l > new_max:
                        new_max = child.max_l
                n.max_l = new_max
            
            answers.append(root.max_l if root.max_l > 0 else 0)
            
            root.count += 1
            for (n, d) in path[1:]:
                n.count += 1
            
            for (n, d) in reversed(path):
                new_max = 0
                if n.count >= k:
                    new_max = d
                for child in n.children.values():
                    if child.max_l > new_max:
                        new_max = child.max_l
                n.max_l = new_max
        
        return answers