class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        pos, negs = len(nums) - bisect_left(nums, 1), bisect_right(nums, -1)
        return max(pos, negs)