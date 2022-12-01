class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n = len(s)
        vawoles = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        half = n//2
        one = 0
        two = 0
        for i in range(n):
            if i < half and s[i] in vawoles:
                one +=1
            elif s[i] in vawoles:
                two += 1
        return one == two