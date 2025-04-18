class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Build adjacency list representing the course dependency graph
        course_graph = [[] for _ in range(numCourses)]
        # No. of prerequisites is not used here but left in original structure
        prereq_count = [0] * numCourses

        for course, prereq in prerequisites:
            course_graph[prereq].append(course)
            prereq_count[course] += 1

        course_order = deque()
        # visited status: 0 = unvisited, 1 = visiting (gray), 2 = visited (black)
        visited = [0] * numCourses

        def dfs(course):
            # If already fully visited, no need to process again
            if visited[course] == 2:
                return True
            # If currently visiting, a cycle is detected
            if visited[course] == 1:
                return False
            # If no outgoing edges (leaf node)
            if course_graph[course] == []:
                visited[course] = 2
                course_order.appendleft(course)
                return True

            # Mark as visiting
            visited[course] = 1
            is_valid = True
            for next_course in course_graph[course]:
                is_valid = is_valid and dfs(next_course)

            # Mark as visited
            visited[course] = 2
            course_order.appendleft(course)

            return is_valid

        has_no_cycle = True
        for i in range(numCourses):
            if visited[i] == 0:
                has_no_cycle = has_no_cycle and dfs(i)

        # Return order if no cycle, otherwise empty list
        return list(course_order) if has_no_cycle else []
