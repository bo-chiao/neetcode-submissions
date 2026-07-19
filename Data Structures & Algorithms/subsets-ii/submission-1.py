class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        current_subset = []

        nums.sort()
        n = len(nums)
        
        def backtrack(start):
            subsets.append(current_subset.copy())

            for i in range(start, n):
                if i > start and nums[i] == nums[i - 1]:
                    continue

                current_subset.append(nums[i])
                backtrack(i + 1)
                current_subset.pop()

        backtrack(0)

        return subsets
        