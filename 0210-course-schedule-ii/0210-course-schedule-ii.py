class Solution:
    def findOrder(self, numCourses: int, pre: List[List[int]]) -> List[int]:
        # return [3,5,4,6,2,0,7,1]
        graph={c:[] for c in range(numCourses)}
        for i in pre:
            graph[i[1]].append(i[0])
        cycle , vis = set(), set()
        output = []
        print(graph)
        for e in graph:
            if e not in vis:
                stk=[e]
                # cycle.add(e)
                while stk:
                    child=False
                    temp=stk[-1]
                    cycle.add(temp)
                    for nb in graph[stk[-1]]:
                        if nb in cycle:
                            print(nb,cycle)
                            return []
                        if nb not in vis:
                            if not child:
                                child=True
                            stk.append(nb)
                    if not child:
                        stk.pop()
                        cycle.remove(temp)
                        if temp not in vis:
                            output.append(temp)
                            vis.add(temp)
        return list(reversed(output))
                
                    