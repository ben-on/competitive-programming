class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = {i:[] for i in range(n)}
        if n == 1: return [0]
        for v1,v2 in edges:
            graph[v1].append(v2)
            graph[v2].append(v1)
        
        leaves = [i for i in graph if len(graph[i])==1]
        while n>2:
            n -= len(leaves)
            temp = []
            for lf in leaves:
                nb = graph[lf].pop()
                graph[nb].remove(lf)
                if len(graph[nb]) == 1:
                    temp.append(nb)
            leaves = temp
        return leaves