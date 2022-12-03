class Solution:
    def numSquares(self, n: int) -> int:
        squares = []
        i = 1
        while i**2<=n:
            squares.append(i**2)
            i+=1
        @cache
        def dp(s):
            if s==0:
                return 0
            if s<0:
                return float('inf')
            return min(1+dp(s-i) for i in squares)
        return dp(n)
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    