class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        ans = [set() for i in range(n)]
        graph = defaultdict(set)
        
        for a, b in edges:
            graph[b].add(a)
        
        
        def dfs(i):
            for neighbor in graph[i]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor)
                    
        
        
        for i in range(n):
            visited = set()
            visited.add(i)
            dfs(i)
            visited.discard(i)
            ans[i] = sorted(visited)
        
        
        return ans