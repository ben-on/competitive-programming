class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)  
        l = 0
        dic = {}
        ans = 0
        for r in range(n):
            dic[s[r]] = dic.get(s[r], 0) + 1

            while len(dic) == 3:
                ans += n - r  
                dic[s[l]] -= 1
                if dic[s[l]] == 0:
                    del dic[s[l]]
                l += 1

        return ans

