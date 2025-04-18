class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Create an adjacency list to represent the graph of course prerequisites
        course_graph = [[] for _ in range(numCourses)]
        # Track the number of prerequisites (in-degree) for each course
        prereq_count = [0] * numCourses

        # Build the graph and populate the prerequisites count
        for course, prereq in prerequisites:
            course_graph[prereq].append(course)
            prereq_count[course] += 1

        # Initialize queue with courses that have no prerequisites
        available_courses = deque([i for i in range(numCourses) if prereq_count[i] == 0])
        course_order = []

        while available_courses:
            num_available = len(available_courses)
            for _ in range(num_available):
                current = available_courses.popleft()
                course_order.append(current)

                # Decrease the prereq count of courses dependent on the current one
                for dependent in course_graph[current]:
                    prereq_count[dependent] -= 1
                    if prereq_count[dependent] == 0:
                        available_courses.append(dependent)

        # If we couldn't schedule all courses, there's a cycle
        if len(course_order) != numCourses:
            return []

        return course_order