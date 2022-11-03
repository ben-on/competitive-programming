class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        dictt = Counter(words)
        ans = 0
        for i in words:
            rev = i[1] + i[0]
            if rev in dictt and dictt[rev] and dictt[i]:
                dictt[rev] -=1
                dictt[i] -=1
                if dictt[i]>=0:
                    ans += 4
        for i in dictt:
            if dictt[i] and i[0] == i[1]:
                ans += 2
                break
        return ans
                
        