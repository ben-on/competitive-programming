class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mm=float('inf')
        p=0
        for i in prices:
            p=max(p,i-mm)
            mm=min(mm,i)
        return p