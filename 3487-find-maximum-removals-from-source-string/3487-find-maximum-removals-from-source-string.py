class Solution:
    def maxRemovals(self, source: str, pattern: str, targetIndices: List[int]) -> int:
        check = 0
        for idx in targetIndices:
            check |= 1 << idx
        
        n, m = len(source), len(pattern)
        memo = [[-1 for i in range(n)] for j in range(n)]

        def dp(i, j):
            if i >= n:
                if j >= m:
                    return 0
                return -float('inf')
            if memo[j][i] != -1:
                return memo[j][i]
            
            
            if j < m and source[i] == pattern[j]:
                
                if  check & (1 << i):
                    left = dp(i + 1, j + 1)
                    right = 1 + dp(i + 1, j)
                    memo[j][i] = max(left, right)
                else:
                    left = dp(i + 1, j + 1)
                    right = dp(i + 1, j)

                    memo[j][i] = max(left, right)
            else:
                if check & (1 << i):
                    memo[j][i] = 1 + dp(i + 1, j)
                else:
                    memo[j][i] = dp(i + 1, j)
            
            return memo[j][i]
        return dp(0,0)
            