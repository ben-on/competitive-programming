class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        s=set(nums)
        a,b=None,None
        ss=set()
        ss.add(nums[0])
        for i in range(1,len(nums)+1):
            if i not in s:
                b=i
            if i< len(nums) and nums[i] in ss:
                a=nums[i]
            elif i< len(nums):
                ss.add(nums[i])
            # print(ss)
        return [a,b]