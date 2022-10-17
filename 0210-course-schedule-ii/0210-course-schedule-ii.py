class Solution:
    def findOrder(self, numCourses: int, pre: List[List[int]]) -> List[int]:
        graph={c:[] for c in range(numCourses)}
        for i in pre:
            graph[i[1]].append(i[0])
        cycle , vis = set(), set()
        output = deque([])
        for e in graph:
            if e not in vis:
                stk=[e]
                while stk:
                    child=False
                    temp=stk[-1]
                    cycle.add(temp)
                    for nb in graph[temp]:
                        if nb in cycle:
                            return []
                        if nb not in vis:
                            if not child:
                                child=True
                            stk.append(nb)
                    if not child:
                        stk.pop()
                        cycle.remove(temp)
                        if temp not in vis:
                            output.appendleft(temp)
                            vis.add(temp)
        return output
                
                    