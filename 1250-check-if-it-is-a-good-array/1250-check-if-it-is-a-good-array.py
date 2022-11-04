class Solution:
    def gcd(self,a,b):
        while a%b != 0:
            mod = a%b
            a = b
            b = mod 
        return b
    def isGoodArray(self, nums: List[int]) -> bool:
        gc = nums[0]
        for i in range(1,len(nums)):
            gc = self.gcd(gc,nums[i])
        return True if gc == 1 else False
            