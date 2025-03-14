class Solution:              
    def checker(self,candies, mx, k):
        if mx == 0:
            return True
        cur = 0
        for candy in candies:  
            cur += candy // mx
        
        return cur  >= k

    def maximumCandies(self, candies: List[int], k: int) -> int:
        l, r = 0, sum(candies)

        while l <= r:
            mid = (l + r) // 2

            if self.checker(candies, mid, k):
                l = mid + 1
            else:
                r = mid - 1
        
        return r