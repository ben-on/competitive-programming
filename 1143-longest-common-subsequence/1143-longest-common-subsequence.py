class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @cache
        def dynamic(i,j):
            if i >= len(text1) or j >= len(text2):
                return 0
            if text1[i] == text2[j]:
                return 1 + dynamic(i+1, j+1)
            return max(dynamic(i+1,j), dynamic(i,j+1))
        return dynamic(0,0)