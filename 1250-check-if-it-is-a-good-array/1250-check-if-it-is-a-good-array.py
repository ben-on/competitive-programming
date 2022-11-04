class Solution:
    def gcd(self,a,b):
        if not a%b:
            return b
        return self.gcd(b,a%b)
    def isGoodArray(self, nums: List[int]) -> bool:
        gc = nums[0]
        for i in range(1,len(nums)):
            gc = self.gcd(gc,nums[i])
        return True if gc == 1 else False
            