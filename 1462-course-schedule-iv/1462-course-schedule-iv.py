class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = [[float('inf') for _ in range(numCourses)] for _ in range(numCourses)]
        for src, dst in prerequisites:
            graph[src][dst] = 1
        # print(graph)
        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    graph[i][j] = min(graph[i][j],graph[i][k]+graph[k][j])
        ans = []
        for q in queries:
            ans.append(graph[q[0]][q[1]]!=float("inf"))
        return ans
                