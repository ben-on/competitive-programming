class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        
        nums.sort()
        print(nums)
        n = len(nums)
        far = n//2
        near = 0
        ans = 0
        while near < n//2 and far < n:
            if nums[near]*2 <= nums[far]:
                ans +=2
                near +=1
                far +=1
            else:
                far +=1
        return ans
            