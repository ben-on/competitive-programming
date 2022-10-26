class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        modIdx = {0:-1}
        t = 0
        for i in range(len(nums)):
            t += nums[i]
            if t%k not in modIdx:
                modIdx[t%k] = i
            elif i - modIdx[t%k] >1:
                return True
        return False