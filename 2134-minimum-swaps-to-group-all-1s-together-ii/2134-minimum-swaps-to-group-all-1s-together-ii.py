class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        l = 0
        r = sum(nums)-1
        zeros = sum([1 for i in range(r+1) if nums[i] == 0 ])
        n = len(nums)
        ans = float('inf')
        while r <(n*2)-1:
            r+=1
            if nums[r%n] == 0:
                zeros+=1
            if nums[l%n] ==0:
                zeros -= 1
            l+=1
            ans = min(ans,zeros)
        return ans
        
        
        
            
        
            