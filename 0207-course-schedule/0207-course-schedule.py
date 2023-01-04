class Solution:
    def canFinish(self, numCourses: int, preq: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indeg = [0]*numCourses
        for ai,bi in preq:
            graph[bi].append(ai)
            indeg[ai] += 1
        
        actual_order = []
        que = deque([])
        for i,ct in enumerate(indeg):
            if ct == 0:
                que.append(i)
        while que:
            temp = que.popleft()
            actual_order.append(temp)
            for nb in graph[temp]:
                indeg[nb] -= 1
                if indeg[nb] == 0:
                    que.append(nb)
        if len(actual_order) != numCourses:
            return []
        return actual_order
            