class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]: return True
        l = 0
        r = len(s) - 1
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                temp1 = s[:l] + s[l+1:]
                temp3 = s[:r] + s[r+1:]
                if temp1 == temp1[::-1] or temp3 == temp3[::-1]:
                    return True
                else:
                    return False
        return True