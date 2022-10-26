class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        modIdx = {0:-1}
        t = 0
        for i in range(len(nums)):
            t += nums[i]
            rm = t%k
            if rm not in modIdx:
                modIdx[rm] = i
            elif i - modIdx[rm] >1:
                return True
        return False