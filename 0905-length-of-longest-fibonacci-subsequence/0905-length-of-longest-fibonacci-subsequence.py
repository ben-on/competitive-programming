class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        vals = {val:idx for idx, val in enumerate(arr)}  
        dic = {}
        
        n  = len(arr)
        ans = 0
        for i in range(n): 
            for j in range(i + 1, n):
                cur_ans = 2 
                a1, a2 = arr[i], arr[j]
                while a1 + a2 in vals:
                    a3 = a1 + a2
                    a1 = a2
                    a2 = a3 
                    cur_ans += 1
                ans = max(cur_ans, ans)
        return ans if ans >= 3 else 0