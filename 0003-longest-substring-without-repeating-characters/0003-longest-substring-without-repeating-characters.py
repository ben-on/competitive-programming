class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        prevs = set()
        left = 0
        ans = 0
        for i in range(len(s)):
            while s[i] in prevs:
                prevs.remove(s[left])
                left += 1
            prevs.add(s[i])
            ans = max(i-left+1,ans)
        return ans 
            
