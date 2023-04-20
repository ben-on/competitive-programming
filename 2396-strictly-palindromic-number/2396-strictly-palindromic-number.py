class Solution:
    
    def numberToBase(self,n, b):
        if n == 0:
            return [0]
        digits = []
        while n:
            digits.append(int(n % b))
            n //= b
            
        return digits[::-1]  == digits 
    def isStrictlyPalindromic(self, n: int) -> bool:
        for i in range(2,n-1):
            if not self.numberToBase(n,i):
                return False
        return True
            