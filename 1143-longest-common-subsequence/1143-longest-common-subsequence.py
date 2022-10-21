class Solution:
    t1,t2=None,None
    @cache
    def dynamic(self,i,j):
        if i >= len(self.t1) or j >= len(self.t2):
            return 0
        if self.t1[i] == self.t2[j]:
            return 1 + self.dynamic(i+1, j+1)
        return max(self.dynamic(i+1,j), self.dynamic(i,j+1))
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        self.t1,self.t2 = text1, text2
        return self.dynamic(0,0)