class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for v1,v2 in edges:
            graph[v1].append(v2)
            graph[v2].append(v1)
        stk = [source]
        vis = {source}
        while stk:
            temp = stk.pop()
            for nb in graph[temp]:
                if nb not in vis :
                    if nb == destination:
                        return True
                    stk.append(nb)
                    vis.add(nb)
        return False if source != destination else True
                    