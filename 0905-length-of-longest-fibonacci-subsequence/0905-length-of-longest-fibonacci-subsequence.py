class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        vals = {val:idx for idx, val in enumerate(arr)}  
        dic = {}
        def dp(a1,a2): 
            if (a1, a2) in dic:  
                return dic[(a1, a2)]
            if a1 + a2 not in vals: 
                return 0
            
            dic[(a1,a2)] = 1 + dp(a2, a1 + a2)

            return dic[(a1,a2)]
        n  = len(arr)
        ans = 0
        for i in range(n): 
            for j in range(i + 1, n):
                cur_ans = 2 + dp(arr[i],arr[j])
                ans = max(cur_ans, ans)
        return ans if ans >= 3 else 0