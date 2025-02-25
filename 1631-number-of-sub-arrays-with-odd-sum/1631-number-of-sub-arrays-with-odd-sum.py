class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        even = 1
        odd = 0
        running_sum = 0
        ans = 0

        for num in arr:
            running_sum += num
            if running_sum % 2:
                ans += even
            else:
                ans += odd
            
            even += running_sum % 2 == 0
            odd += running_sum % 2 == 1
        
        return ans %  (10**9 + 7)