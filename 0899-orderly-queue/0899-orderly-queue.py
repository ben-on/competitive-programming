class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        tar = sorted(s)
        n = len(s)
        if k > 1:
            return "".join(tar)
        ans = s
        for i in range(n):
            s = s[1:] + s[0]
            ans = min(ans,s)
        return ans
        