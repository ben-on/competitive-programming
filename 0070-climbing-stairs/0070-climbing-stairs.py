class Solution:
    dp={}
    def climbStairs(self, n: int) -> int:
        @lru_cache
        def dfs(val):
            if val >= n:
                return 1 if val == n else 0
            return dfs(val+1) + dfs(val+2)
        return dfs(0)