class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        path = []

        visited = set()

        def backtrack():
            if len(path) == len(nums):
                permutations.append(path.copy())
                return

            for num in nums:
                if num in visited:
                    continue

                path.append(num)
                visited.add(num)
                
                backtrack()
                
                path.pop()
                visited.remove(num)

        backtrack()
        
        return permutations
