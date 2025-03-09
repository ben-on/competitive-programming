class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        ans = 0
        cur = 1
        n = len(colors)

        for i in range(1,n + k - 1):
            if colors[i % n] != colors[(i - 1) % n]:
                cur += 1
            else:
                cur = 1

            if cur >= k:
                ans +=1
        
        return ans