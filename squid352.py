class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res, s = -float('inf'),  0
        for elem in nums:
            if s < 0:
                s = elem
            else:
                s = s + elem
            res = max(res, s)
        return res
