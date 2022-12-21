class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for v1,v2 in dislikes:
            graph[v1].append(v2)
            graph[v2].append(v1)
        vis = set()
        colors = {}
        for i in graph:
            if i not in vis:
                vis.add(i)
                colors[i] = False
                stk = [i]
                while stk:
                    temp = stk.pop()
                    for nb in graph[temp]:
                        if nb not in vis:
                            stk.append(nb)
                            colors[nb] = not colors[temp]
                            vis.add(nb)
                        elif colors[nb] == colors[temp]:
                            return False
        return True
                
            