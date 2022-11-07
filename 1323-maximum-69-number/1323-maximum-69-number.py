class Solution:
    def maximum69Number (self, num: int) -> int:
        p = 0
        orig = num
        last = 0
        while num:
            r = num % 10
            num = num // 10
            if r == 6:
                last = 10**p
            p +=1
        return orig + (3*last)
        