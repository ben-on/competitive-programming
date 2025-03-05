class Solution:
    def coloredCells(self, n: int) -> int:
        res = 1
        i = 0   
    
        while i <  n:        
            res += (i * 4)  
            i += 1

        return res 
