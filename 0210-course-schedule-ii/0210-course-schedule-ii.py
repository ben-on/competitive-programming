class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for i in range(numCourses)]
        pres = [0] * numCourses

        for course, pre in prerequisites:
            graph[pre].append(course)
            pres[course] += 1
        
        ans = []
        visited = [0] * numCourses
        # 0 means not visited, 1 is gray, 2 is black

        def dfs(node):
            if visited[node] == 2:
                return True
                
            if graph[node] == []:
                visited[node] = 2
                ans.append(node)
                return True

            if visited[node] == 1:
                return False

            visited[node] = 1
            res = True
            for child in graph[node]:
                res = res and dfs(child)
            
            visited[node] = 2
            ans.append(node)

            return res
        
        nocycle = True

        for i in range(numCourses):
            if visited[i] == 0:
                nocycle = nocycle and dfs(i)
        
        if nocycle:
            return ans[::-1]
        
        return []
                

            