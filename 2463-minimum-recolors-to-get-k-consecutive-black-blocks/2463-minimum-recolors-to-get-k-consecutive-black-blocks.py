class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        whites  = ans = blocks[:k].count('W') 
        l = 0  

        for r in range(k, len(blocks)):
            whites += blocks[r] == 'W'
            whites -= blocks[l] == 'W' 
            l += 1
            ans = min(ans, whites) 
        
        return ans

