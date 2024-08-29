class Solution:
    def findComplement(self, num: int) -> int:
        nu = 0
        i = 0
        while num:
            if not (num & 1):
                nu |= (1 << i)
            i += 1
            num = num >> 1 
        return nu