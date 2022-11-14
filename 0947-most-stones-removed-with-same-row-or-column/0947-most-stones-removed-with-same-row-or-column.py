class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        graph = defaultdict(set)
        n = len(stones)
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                if stones[i][0]==stones[j][0] or stones[i][1] == stones[j][1]:
                    graph[i].add(j)
                    graph[j].add(i)
        vis = set()
        c = 0
        for i in range(n):
            if i not in vis:
                stk = [i]
                tvis = {i}
                while stk:
                    temp = stk.pop()
                    vis.add(temp)
                    for nb in graph[temp]:
                        if nb not in tvis:
                            stk.append(nb)
                            tvis.add(nb)
                c+=1
        return n-c
        
        