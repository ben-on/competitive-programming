class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Step 1: Reverse graph: course -> list of its prerequisites
        graph = defaultdict(list)
        inDegree = [0] * numCourses

        for course, prereq in prerequisites:
            graph[course].append(prereq)
            inDegree[prereq] += 1

        # Step 2: Start with courses that have no prerequisites
        queue = deque([i for i in range(numCourses) if inDegree[i] == 0])
        order = []

        # Step 3: Process courses with no remaining prerequisites
        while queue:
            course = queue.popleft()
            order.append(course)

            # For each course that depends on this one, reduce their in-degree
            for dependent in graph[course]:
                inDegree[dependent] -= 1
                if inDegree[dependent] == 0:
                    queue.append(dependent)

        # If all courses are taken, return order; else return empty list
        return order[::-1] if len(order) == numCourses else []