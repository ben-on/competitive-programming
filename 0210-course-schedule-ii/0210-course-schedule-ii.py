class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for i in range(numCourses)]
        pres = [0] * numCourses

        for course, pre in prerequisites:
            graph[pre].append(course)
            pres[course] += 1
        

        que = deque([i for i in range(numCourses) if pres[i] == 0])
        ans = []
        while que:
            r = len(que)
            for i in range(r):
                temp = que.popleft()
                ans.append(temp)
                for child in graph[temp]:
                    pres[child] -= 1
                    if pres[child] == 0:
                        que.append(child)
                
        if len(ans) != numCourses:
            return []
        
        return ans

                
