class Solution:
    def jump(self, nums: List[int]) -> int:
        l = len(nums)
        stack = [0] + [9999] * (l - 2)
        for i in range(l - 1):
            for j in range(i + 1, i + nums[i] + 1):
                if i + nums[i] >= l - 1:
                    return stack[i] + 1
                stack[j] = min(stack[j], stack[i] + 1)
        return stack[l - 2]