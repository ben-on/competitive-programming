class Solution:
    def check(self, word, pattern):
        n = len(word)
        mat = {}

        for i in range(n):
            if word[i] in mat and mat[word[i]] != pattern[i]:
                return False
            if word[i] not in mat:
                mat[word[i]] = pattern[i]
        
        return True

    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:

        ans = []

        for word in words:
            if self.check(word, pattern) and self.check(pattern, word):
                ans.append(word)
        
        return ans
        