class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s=set()
        for i in range(len(nums)):
            if target-nums[i] in s:
                return [i,nums.index(target-nums[i])]
            s.add(nums[i])
                
        