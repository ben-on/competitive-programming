class Solution:
    def maxSum(self, nums: List[int], k: int, m: int) -> int:
        n = len(nums)
        memo = [[0 for i in range(n + 1)] for j in range(n + 1)]
        pref = list(accumulate(nums, initial=0))
        @cache
        def dp(cnt, idx, bl):
            if n - idx < (k - cnt) * m:
                return -inf
            if idx >= n:
                if cnt == k:
                    return 0
                return -inf
            
            ans = dp(cnt, idx + 1, False)
            if bl:
                ans = max(ans, nums[idx] + dp(cnt, idx + 1, bl))
            
            if idx + m <= n:
                ans = max(ans, pref[idx + m] - pref[idx] + dp(cnt + 1, idx + m, True))

            
            return ans
        
        res = dp(0,0, False)
        dp.cache_clear()

        return res
                


