class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        # print(nums)
        while len(nums)>=3:
            s1=nums.pop()
            s2=nums[-1]
            s3=nums[-2]
            if s3+s2>s1 and s1+s3>s2 and s2+s1>s3:
                return sum([s1,s2,s3])
        return 0
                
            