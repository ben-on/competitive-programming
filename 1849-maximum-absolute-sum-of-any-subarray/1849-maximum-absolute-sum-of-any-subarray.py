class Solution:
    def findmin(self, arr):
        ans = min(arr) 
        prevmax = 0
        running = 0
        

        for num in arr:
            running += num
            ans = min(running - prevmax, ans)
            prevmax = max(running, prevmax)

        return ans



    def maxAbsoluteSum(self, nums: List[int]) -> int:
        ans = max(nums) 
        prevmin = 0
        running = 0
        

        for num in nums:
            running += num
            ans = max(running - prevmin, ans)
            prevmin = min(running, prevmin)
        
        return max(abs(ans), abs(self.findmin(nums)))