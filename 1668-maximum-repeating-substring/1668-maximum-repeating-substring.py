class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        cur = word
        ans = 0
        while 1:
            if cur in sequence:
                ans +=1
                cur += word
            else:
                break
        return ans