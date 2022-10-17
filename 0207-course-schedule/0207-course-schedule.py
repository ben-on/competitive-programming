class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {course :[] for course in range(numCourses)}
        for prerequest in prerequisites:
            graph[prerequest[1]].append(prerequest[0])
        vis, cycle = set(), set()
        for course in range(numCourses):
            if course not in vis:
                stk = [course]
                while stk:
                    temp=stk[-1]
                    cycle.add(temp)
                    child=False
                    for nb in graph[temp]:
                        if nb in cycle:
                            return False
                        if nb not in vis:
                            if not child :
                                child=True
                            stk.append(nb)
                    if not child:
                        stk.pop()
                        cycle.remove(temp)
                        vis.add(temp)
        return True
                            