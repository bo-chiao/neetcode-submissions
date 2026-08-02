class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)

        for crs, pre in prerequisites:
            adj[pre].append(crs)

        course_seq = []

        state = [0] * numCourses
        
        def hasCycle(crs):
            if state[crs] == 1:
                return True

            if state[crs] == 2:
                return False

            state[crs] = 1

            for next_crs in adj[crs]:
                if hasCycle(next_crs):
                    return True

            state[crs] = 2
            course_seq.append(crs)

            return False

        for crs in range(numCourses):
            if hasCycle(crs):
                return []

        return course_seq[::-1]
