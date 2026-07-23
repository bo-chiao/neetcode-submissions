class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def isPalindrom(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1

            return True

        results = []

        def backtrack(l, path):
            if l == len(s):
                results.append(path.copy())

            for r in range(l, len(s)):
                if isPalindrom(l, r):
                    path.append(s[l : r + 1])
                    backtrack(r + 1, path)
                    path.pop()

        backtrack(0, [])
        return results
        