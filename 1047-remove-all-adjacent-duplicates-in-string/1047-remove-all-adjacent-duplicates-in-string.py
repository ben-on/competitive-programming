class Solution:
    def removeDuplicates(self, s: str) -> str:
        stk = []
        for i in s:
            if stk and i == stk[-1]:
                stk.pop()
            else:
                stk.append(i)
        return "".join(stk)