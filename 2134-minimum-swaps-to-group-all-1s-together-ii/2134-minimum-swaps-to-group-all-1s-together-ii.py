class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        new = nums + nums
        l = 0
        r = sum(nums)-1
        zeros = sum([1 for i in range(r+1) if new[i] == 0 ])
        n = len(new)
        ans = float('inf')
        while r < n-1:
            r+=1
            if new[r] == 0:
                zeros+=1
            if new[l] ==0:
                zeros -= 1
            l+=1
            ans = min(ans,zeros)
        return ans
        
        
        
            
        
            