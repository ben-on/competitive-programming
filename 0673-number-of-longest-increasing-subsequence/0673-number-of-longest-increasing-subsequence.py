class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        dpc = [1] * n


        for i in range(n - 1, -1 , -1):
            val = 0
            cnt = 0
            for j in range(i+1, n):
                if nums[j] > nums[i]:
                    if dp[j] > val:
                        val = dp[j]
                        cnt = dpc[j]
                    elif dp[j] == val:
                        cnt += dpc[j]
            dp[i] += val
            dpc[i] = max(1,cnt)
        mx = max(dp)
        ans = 0
        for i in range(n):
            if dp[i] == mx:
                ans += dpc[i]
        return ans
        