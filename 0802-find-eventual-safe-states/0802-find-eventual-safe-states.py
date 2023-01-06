class Solution:
    def hascycle(self,cur_node,graph,color): 
        if color[cur_node] == 1:
            return True
        if color[cur_node] == 2:
            return False
        color[cur_node] = 1
        for nb in graph[cur_node]:
            cfound = self.hascycle(nb,graph,color)
            if cfound :
                return True
        
        color[cur_node] = 2
        return False
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        colors = [0]*n
        for i in range(n):
            if colors[i] != 2:
                self.hascycle(i,graph,colors)
        
        return [i for i in range(n) if colors[i]==2]
    