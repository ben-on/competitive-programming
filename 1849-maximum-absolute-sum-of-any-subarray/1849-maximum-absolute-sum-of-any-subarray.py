class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        ans = max(nums) 
        ans2 = min(nums)
        prevmin = 0
        prevmax = 0
        running = 0
        

        for num in nums:
            running += num
            ans = max(running - prevmin, ans)
            ans2 = min(running - prevmax, ans2)
            prevmin = min(running, prevmin)
            prevmax = max(running, prevmax)
        
        return max(abs(ans), abs(ans2))