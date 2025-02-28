class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)
        @cache
        def dp(i, j):
            if i >= n or j >= m:
                return 0
            
            if text1[i] == text2[j]:
                choose = 1 + dp(i+1, j+1)
                notchoose = max(dp(i + 1, j), dp(i, j + 1)) 
                return max(choose, notchoose)
            notchoose = max(dp(i + 1, j), dp(i, j + 1))
            choose = dp(i+1, j+1) 

            return max(choose, notchoose)
        
        return dp(0,0)