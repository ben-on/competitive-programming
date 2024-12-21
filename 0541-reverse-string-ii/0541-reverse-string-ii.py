class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        ans = []
        n = len(s)

        i = 0

        while i < n:
            for j in range(min(i + k - 1, n - 1), i - 1, -1):
                ans.append(s[j])
            for a in range(i + k, min(n, i + (2 * k))):
                ans.append(s[a])

            i += 2 * k
        
        return "".join(ans)

