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
    def eventualSafeNodes(self, g: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        n = len(g)
        
        for i in range(len(g)):
            graph[i] = g[i]
            
        colors = [0]*n
        for i in range(n):
            if colors[i] != 2:
                self.hascycle(i,graph,colors)
        
        return [i for i in range(n) if colors[i]==2]
        
        
        
# class Solution:
#     def hascycle(self,cur_node,graph,color): 
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
#     def canFinish(self, numCourses: int, preq: List[List[int]]) -> bool:
#         graph = defaultdict(list)
        
        
#         for ai,bi in preq:
#             graph[bi].append(ai)
            
#         colors = [0]*numCourses
#         for i in range(numCourses):
#             if colors[i] != 2:
#                 cycle_found = self.hascycle(i,graph,colors)
#                 if cycle_found:
#                     return False
#         return True