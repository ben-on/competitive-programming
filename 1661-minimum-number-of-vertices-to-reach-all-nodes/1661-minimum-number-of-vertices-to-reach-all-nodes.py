class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(int)
        
        for one, two in edges:
            graph[two] += 1
        
        ans = []
        for i in range(n):
            if graph[i] == 0:
                ans.append(i)

        return ans