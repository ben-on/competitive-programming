class Solution:
    def max_divisor(self, n):
        max_div = 1  
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                max_div = max(max_div, i, n // i if n // i < n else 0)
        
        return max_div
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        mm = nums[-1]
        ans = 0
        for i in range(n - 2, -1, -1):
            while mm < nums[i]:
                divi =  self.max_divisor(nums[i])
                if divi == 1:
                    return -1
                
                nums[i] = nums[i] // divi
                ans += 1
            
            mm = min(mm, nums[i])
        
        return ans
            
        