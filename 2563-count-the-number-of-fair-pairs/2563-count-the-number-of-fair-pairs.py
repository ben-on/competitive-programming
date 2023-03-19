class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        n = len(nums)
        ans = 0
        for i in range(n):
            left = bisect_left(nums,lower-nums[i])
            right = bisect_right(nums,upper-nums[i])
            ans += right - left
            if left <= i <right:
                ans -=1
        return ans //2
                    