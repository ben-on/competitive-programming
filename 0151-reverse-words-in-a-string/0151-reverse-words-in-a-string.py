class Solution:
    def reverseWords(self, s: str) -> str:
        lst = s.split()
        return " ".join(list(reversed(lst)))