class Solution:
    def hascycle(self,graph,node,color,level,ans):
        # print()
        if node == -1:
            return 
        if color[node] >0:
            ans.append(level - color[node]+1)
            return True
        if color[node] < 0:
            return False
        
        color[node] = level + 1
        
        cfound = self.hascycle(graph,graph[node],color,color[node],ans)
            
        color[node] = -1
        return False
    def longestCycle(self, edges: List[int]) -> int:
        n = len(edges)
        colors = [0]*n
        ans = []
        
        for i in range(n):
            if colors[i] != 2:
                cycle_found = self.hascycle(edges,i,colors,1,ans)
    
        return max(ans) if ans else -1
