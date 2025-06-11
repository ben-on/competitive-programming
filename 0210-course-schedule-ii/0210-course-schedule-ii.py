class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Build the graph and in-degree count
        graph = defaultdict(list)
        inDegree = [0] * numCourses

        for dest, src in prerequisites:
            graph[src].append(dest)
            inDegree[dest] += 1

        # Queue for nodes with no incoming edges
        queue = deque([i for i in range(numCourses) if inDegree[i] == 0])
        order = []

        while queue:
            course = queue.popleft()
            order.append(course)

            for neighbor in graph[course]:
                inDegree[neighbor] -= 1
                if inDegree[neighbor] == 0:
                    queue.append(neighbor)

        # If all courses are in the order, return it. Otherwise, return empty list (cycle exists)
        return order if len(order) == numCourses else []