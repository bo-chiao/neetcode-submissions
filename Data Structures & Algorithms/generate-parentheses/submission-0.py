class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        results = []

        def backtrack(left_count, right_count, current_string):
            if len(current_string) == n * 2:
                results.append(current_string)

            if left_count < n:
                backtrack(left_count + 1, right_count, current_string + "(")
                
            if right_count < left_count:
                backtrack(left_count, right_count + 1, current_string + ")")
        
        backtrack(0, 0, "")

        return results
