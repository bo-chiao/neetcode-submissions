class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = []
        current_combination = []

        candidates.sort()
        n = len(candidates)

        def backtrack(start, remaining):
            if remaining < 0:
                return
            
            if remaining == 0:
                combinations.append(current_combination.copy())
                return

            for i in range(start, n):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                current_combination.append(candidates[i])
                backtrack(i + 1, remaining - candidates[i])
                current_combination.pop()

        backtrack(0, target)

        return combinations
