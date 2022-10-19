class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        wind=set()
        left=0
        ans=0
        for i in range(len(s)):
            while s[i] in wind:
                wind.remove(s[left])
                left+=1
            ans=max(ans,i-left+1)
            wind.add(s[i])
        return ans
