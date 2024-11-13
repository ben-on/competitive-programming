class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        n = len(s)
        l = 0
        freq = defaultdict(int)
        ans = 0
        for r in range(n):
            freq[s[r]] += 1

            
            while freq[s[r]] == k:
                freq[s[l]] -= 1
                l += 1
                ans += n - r
        
        return ans
            
    
            