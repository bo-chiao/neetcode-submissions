class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])
        l, r = 0, n * m - 1

        while l <= r:
            i = (l + r) // 2
            col = i % m
            row = i // m
            
            num = matrix[row][col]
            if num == target:
                return True
            elif num < target:
                l = i + 1
            else:
                r = i - 1

        return False
