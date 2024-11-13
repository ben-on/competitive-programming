class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            temp = []
            for i in range(num.bit_length()):
                new = num & ~(1 << i)
                if new | (new + 1) == num:
                    temp.append(new)
 
            if temp:
                ans.append(min(temp))
            else:
                ans.append(-1)
        
        return ans