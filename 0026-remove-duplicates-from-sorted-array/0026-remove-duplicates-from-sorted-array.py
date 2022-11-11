class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        s=sorted(list(set(nums)))
        for i in range(len(nums)):
            if i >= len(s):
                # nums[i]="_"
                continue
            nums[i]=s[i]
        return len(s)