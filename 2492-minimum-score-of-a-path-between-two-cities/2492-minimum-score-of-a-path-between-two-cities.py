class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        dist = {}
        for a,b,s in roads:
            graph[a].append((b,s))
            graph[b].append((a,s))
        stk = [1]
        ans = float('inf')
        vis = set()
        while stk:
            temp = stk.pop()
            for nb,d in graph[temp]:
                if (nb,temp) not in vis and (temp,nb) not in vis:
                    stk.append(nb)
                    vis.add((nb,temp))
                    ans = min(ans,d)
        return ans
            
        
            