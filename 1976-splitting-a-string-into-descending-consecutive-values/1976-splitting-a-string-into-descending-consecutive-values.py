class Solution:
    def splitString(self, s: str) -> bool:
        n = len(s)
        stk = []

        def back(idx):
            if idx >= n:
                return len(stk) >= 2
            
            for i in range(idx, n):
                cur = s[idx:i+1]

                if len(stk) == 0 or stk[-1] - int(cur) == 1:
                    stk.append(int(cur))
                    if back(i+1):
                        return True
                    stk.pop()
            
            return False
        
        return back(0)

