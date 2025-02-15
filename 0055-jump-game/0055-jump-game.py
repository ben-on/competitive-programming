class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if nums[0] == 0 and len(nums) > 1:
            return False

        mx = nums[0] - 1

        for i in range(1, len(nums) - 1):
            if nums[i] == 0 and mx == 0:
                return False
            mx = max(nums[i], mx)
            mx -= 1
        
        return True