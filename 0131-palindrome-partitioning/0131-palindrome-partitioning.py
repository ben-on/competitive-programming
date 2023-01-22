class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        stk = [[[s[0]],0]]
        ans = []
        while stk:
            tmpl,idx = stk.pop()
            if idx == n-1:
                if list(tmpl[-1]) == list(reversed(tmpl[-1])):
                    ans.append(tmpl)
                continue
            if list(tmpl[-1]) == list(reversed(tmpl[-1])):
                stk.append([tmpl+[s[idx+1]],idx+1])
                tmpl[-1] += s[idx+1]
                stk.append([tmpl,idx+1])
            else:
                tmpl[-1] += s[idx+1]
                stk.append([tmpl,idx+1])
        return ans
                