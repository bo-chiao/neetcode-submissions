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
        n = len(s)
        
        def backtrack(start, path):
            if start == n:
                results.append(path.copy())
                return

            for end in range(start, n):
                if isPalindrom(start, end):
                    path.append(s[start : end + 1])
                    backtrack(end + 1, path)
                    path.pop()

        backtrack(0, [])

        return results
