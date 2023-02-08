class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        deg = defaultdict(int)
        for v1,v2 in adjacentPairs:
            graph[v1].append(v2)
            deg[v1] +=1
            graph[v2].append(v1)
            deg[v2] +=1
        que = deque([])
        for i in graph:
            if deg[i] == 1:
                que.append(i)
                break
        vis = set()
        print(graph,que,deg)
        ans = deque([])
        while que:
            temp = que.popleft()
            ans.append(temp)
            vis.add(temp)
            for nb in graph[temp]:
                if nb not in vis:
                    deg[nb] -=1
                    if deg[nb] == 1 or deg[nb]==0:
                        que.append(nb)
        return ans
                
                    