class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp={}
        def profit(idx,bl):
            if idx>=len(prices):
                return 0
            if (idx,bl) in dp:
                return dp[(idx,bl)]
            cooldown= profit(idx+1,bl)
            if bl:
                buy=profit(idx+1,False)-prices[idx]
                dp[(idx,bl)]=max(cooldown,buy)
            else:
                sell=profit(idx+2,True)+prices[idx]
                dp[(idx,bl)]=max(cooldown,sell)
            return dp[(idx,bl)]
        return profit(0,True)
