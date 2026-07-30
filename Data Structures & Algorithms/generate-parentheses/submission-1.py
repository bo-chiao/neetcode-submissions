class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        results = []

        def backtrack(l, r, path):
            if len(path) == 2 * n:
                results.append(path)
                return

            if l > r:
                backtrack(l, r + 1, path + ")")

            if l < n:
                backtrack(l + 1, r, path + "(")

        backtrack(0, 0, "")
        return results
