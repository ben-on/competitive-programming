class TrieNode:
    def __init__(self,b=False):
        self.childs={}
        self.isend=b
        
class Trie:

    def __init__(self):
        self.words=TrieNode()

    def insert(self, word: str) -> None:
        def check(idx,node):
            if idx==len(word):
                return 
            if word[idx] not in node.childs:
                node.childs[word[idx]]=TrieNode()
            if idx==len(word)-1:
                node.childs[word[idx]].isend=True
            return check(idx+1,node.childs[word[idx]])
        check(0,self.words)
    def search(self, word: str) -> bool:
        curr=self.words
        for i in range(len(word)):
            if i==len(word)-1 and word[i] in curr.childs and curr.childs[word[i]].isend:
                return True
            if word[i] in curr.childs:
                curr=curr.childs[word[i]]
            else:
                return False
        return False
    def startsWith(self, prefix: str) -> bool:
        curr=self.words
        for i in range(len(prefix)):
            if i==len(prefix)-1 and prefix[i] in curr.childs:
                return True
            if prefix[i] in curr.childs:
                curr=curr.childs[prefix[i]]
            else:
                return False
        return False


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)