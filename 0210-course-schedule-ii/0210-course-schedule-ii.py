class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Build an adjacency list to represent the course dependency graph
        course_graph = [[] for _ in range(numCourses)]
        # Track the number of prerequisites for each course
        prereq_count = [0] * numCourses

        # Populate the graph and prereq_count list
        for course, prereq in prerequisites:
            course_graph[prereq].append(course)
            prereq_count[course] += 1

        # Initialize a queue with courses that have no prerequisites
        queue = deque([i for i in range(numCourses) if prereq_count[i] == 0])
        # This will store the final course order
        course_order = []

        while queue:
            # Pop a course with no remaining prerequisites
            current_course = queue.popleft()
            course_order.append(current_course)

            # Reduce the prereq count of its dependent courses
            for dependent in course_graph[current_course]:
                prereq_count[dependent] -= 1
                # If a dependent course has no more prerequisites, add it to the queue
                if prereq_count[dependent] == 0:
                    queue.append(dependent)

        # If all courses are accounted for, return the valid order; else return empty list
        return course_order if len(course_order) == numCourses else []
