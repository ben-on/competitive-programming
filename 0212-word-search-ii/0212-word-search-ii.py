class TrieNode:
    def __init__(self) -> None:
        self.word = None
        self.children = defaultdict(TrieNode)
        self.wordCount = 0
    
    def addWord(self, w) -> None:
        cur = self
        cur.wordCount += 1

        for c in w:
            cur = cur.children[c]
            cur.wordCount += 1
        
        cur.word = w
    
    def removeWord(self, w) -> None:
        cur = self
        cur.wordCount -= 1

        for c in w:
            cur = cur.children[c]
            cur.wordCount -= 1        
        

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        n, m = len(board), len(board[0])
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        ans = set()
        vis = set()

        root = TrieNode()

        # build trie
        for word in words:
            root.addWord(word)

        def dfs(i, j, currNode):
            if (i < 0
            or i >= n
            or j < 0
            or j >= m #out of bounds checks
            or (i, j) in vis # have we vis?
            or board[i][j] not in currNode.children 
            or currNode.children[board[i][j]].wordCount < 1
            ): return

            currChar = board[i][j]
            currNode = currNode.children[currChar]
            vis.add((i, j))

            if currNode.word and currNode.word not in ans:
                ans.add(currNode.word)
                root.removeWord(currNode.word) 
            
            for x, y in dirs:
                ix = i + x
                yj = j + y

                dfs(ix, yj, currNode)

            vis.remove((i, j)) 
        for i in range(n):
            for j in range(m):
                dfs(i, j, root)
        
        return ans



