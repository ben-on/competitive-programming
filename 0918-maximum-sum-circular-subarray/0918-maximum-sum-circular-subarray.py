class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        if max(nums)<=0:
            return max(nums)
        find_max=[i for i in nums]
        find_min=[j for j in nums]
        for r in range(1,len(nums)):
            if find_max[r-1]>0:
                find_max[r]+=find_max[r-1]
            if find_min[r-1]<0:
                find_min[r]+=find_min[r-1]
        return max(max(find_max),sum(nums)-min(find_min))