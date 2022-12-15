class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n,m = len(text1),len(text2)
        @cache
        def dfs(i,j):
            if i >= n or j >= m:
                return 0
            if text1[i] == text2[j]:
                return max(1+dfs(i+1,j+1),dfs(i+1,j),dfs(i,j+1))
            else:
                return max(dfs(i+1,j),dfs(i,j+1))
        return dfs(0,0)
        # # the tabulation method
        # dp = [[0 for i in text1] for j in text2]
        # cur = 0
        # n,m = len(text2),len(text1)
        # for i in range(m):
        #     if text2[0] == text1[i]:
        #         cur += 1
        #     dp[0][i] = cur
        # cur = 0
        # for i in range(n):
        #     if text1[0] == text2[i]:
        #         cur += 1
        #     dp[i][0] = cur
        # for i in range(1,n):
        #     for j in range(1,m):
        #         if text1[j] == text2[i]:
        #             dp[i][j] = 1+dp[i-1][j-1]
        #         else:
        #             dp[i][j] = dp[i-1][j-1]
        # return max(dp[-1])