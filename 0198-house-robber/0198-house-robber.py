class Solution:
    dp={}
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        @lru_cache
        def dfs(idx):
            if idx >= n:
                return 0
            return max(dfs(idx+1),nums[idx]+dfs(idx+2))
        return dfs(0)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # n = len(nums)
        # @cache
        # def dfs(idx):
        #     if idx >= n:
        #         return 0
        #     return max(nums[idx]+dfs(idx+2),dfs(idx+1))
        # return dfs(0)