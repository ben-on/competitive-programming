class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        right = 2**(n - 1)
        # print(right)
        left = 1
        i = 1
        cur = 0
        
        while i < n:
            mid = (left + right) // 2
            
            if mid < k:
                left = mid
                cur = 0 if cur == 1 else 1
            else:
                right = mid
                cur = 1 if cur == 1 else 0
            # print('mid', mid, 'level', i+1, 'val', cur)
            
            i += 1
            
        
        return cur
                
            
                
            
        