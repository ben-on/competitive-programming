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
        print(ans,colors)
        return max(ans) if ans else -1
#      def hascycle(self,cur_node,graph,color): 
#         if color[cur_node] == 1:
#             return True
#         if color[cur_node] == 2:
#             return False
#         color[cur_node] = 1
#         for nb in graph[cur_node]:
#             cfound = self.hascycle(nb,graph,color)
#             if cfound :
#                 return True
        
#         color[cur_node] = 2
#         return False