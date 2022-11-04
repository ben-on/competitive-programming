class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {'a','A','e','E','i','I','o','O','u','U'}
        
        vw = []
        for i in s:
            if i in vowels:
                vw.append(i)
        new = []
        for i in s:
            if i in vowels:
                new.append(vw.pop())
            else:
                new.append(i)
        return "".join(new)
            