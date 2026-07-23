class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
            
        num_letter_map = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

        results = []

        def backtrack(index, path):
            if len(path) == len(digits):
                results.append(path)
                return

            for letter in num_letter_map[digits[index]]:
                backtrack(index + 1, path + letter)

        backtrack(0, "")
        return results
        