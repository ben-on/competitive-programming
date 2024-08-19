class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        changed.sort()
        
        stk = deque([])
        ans = []
        for i in changed:
            if stk and stk[0] * 2 == i:
                ans.append(stk.popleft())
            else:
                stk.append(i)
        
        return ans if not stk else []