# time and space analysis
# time: O(n)
# space: O(n)
class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        pre = 0
        tot = sum(nums)
        n = len(nums)
        
        ans = float('inf')
        ansI = None
        for i in range(n):
            pre += nums[i]
            avpre = pre//(i+1)
            avpost = (tot-pre)//(n-i-1) if i<n-1 else 0
            tar = abs(avpre-avpost)
            if tar < ans:
                ans = tar
                ansI = i
        return ansI
    