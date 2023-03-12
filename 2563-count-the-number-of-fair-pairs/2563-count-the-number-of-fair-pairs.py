class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        def count(arr, upper):
            left = 0
            count_ = 0
            size = len(arr)
            for right in range(1, size):
                while left >= 0 and arr[left] + arr[right] > upper:
                    left -= 1
                count_ += left
                left += 1
            return count_

        def fair_pairs(arr, lower, upper):
            arr.sort()
            count_lower = count(arr, lower - 1)
            count_upper = count(arr, upper)
            return count_upper - count_lower

        return fair_pairs(nums, lower,upper)