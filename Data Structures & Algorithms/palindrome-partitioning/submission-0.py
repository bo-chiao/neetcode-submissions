class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def isPalindrom(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1

            return True

        results = []
        n = len(s)

        def backtrack(start, path):
            if start == n:
                results.append(path.copy())
                return

            for i in range(start, n):
                if isPalindrom(start, i):
                    path.append(s[start : i + 1])
                    backtrack(i + 1, path)
                    path.pop()

        backtrack(0, [])

        return results
        