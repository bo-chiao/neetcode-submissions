class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combinations = []
        current_combination = []
        n = len(nums)

        def backtrack(start, remaining):
            if remaining < 0:
                return

            if remaining == 0:
                combinations.append(current_combination.copy())
                return

            for i in range(start, n):
                current_combination.append(nums[i])
                backtrack(i, remaining - nums[i])
                current_combination.pop()

        backtrack(0, target)

        return combinations
