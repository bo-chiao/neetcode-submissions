class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = defaultdict(list)

        for course, pre in prerequisites:
            adj_list[pre].append(course)

        state = [0] * numCourses

        def hasCycle(i):
            if state[i] == 2:
                return False
            
            if state[i] == 1:
                return True

            state[i] = 1

            for course in adj_list[i]:
                if hasCycle(course):
                    return True

            state[i] = 2
            return False

        for i in range(numCourses):
            if hasCycle(i):
                return False

        return True
        