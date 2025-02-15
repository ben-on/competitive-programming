class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        memo = [False] * n
        memo[-1] = True

        for i in range(n - 2, -1, -1):
            
            for j in range(i + 1, min(i + nums[i] + 1, n) ):
                memo[i] = memo[i] or memo[j]
                if memo[i] == True:
                    break
            
        return memo[0]