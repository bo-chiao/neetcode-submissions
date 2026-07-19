class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        path = []

        def backtrack():
            if len(nums) == 0:
                permutations.append(path.copy())
                return

            for i in range(len(nums)):
                num = nums.pop(i)
                path.append(num)
                backtrack()
                nums.insert(i, num)
                path.pop()

        backtrack()
        
        return permutations
