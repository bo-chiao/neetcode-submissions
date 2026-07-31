class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        
        for course, pre in prerequisites:
            adj[pre].append(course)

        status = [0] * numCourses

        def hasCycle(course):
            if status[course] == 2:
                return False

            if status[course] == 1:
                return True

            status[course] = 1

            for next_course in adj[course]:
                if hasCycle(next_course):
                    return True

            status[course] = 2

            return False

        for course in range(numCourses):
            if hasCycle(course):
                return False

        return True
