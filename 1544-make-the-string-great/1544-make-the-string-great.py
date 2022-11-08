class Solution:
    def makeGood(self, s: str) -> str:
        stk = []
        for i in s:
            if stk and stk[-1] != i and stk[-1].lower() == i.lower():
                stk.pop()
            else:
                stk.append(i)
        return "".join(stk)