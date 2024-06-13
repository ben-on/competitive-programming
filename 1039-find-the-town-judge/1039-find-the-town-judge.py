class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        indeg = defaultdict(int)
        outdeg = defaultdict(int)

        for trusts, trusted in trust:
            indeg[trusts] += 1
            outdeg[trusted] += 1
        
        for i in range(1,n+1):
            if indeg[i] == 0 and outdeg[i] == n - 1:
                return i
        
        return -1