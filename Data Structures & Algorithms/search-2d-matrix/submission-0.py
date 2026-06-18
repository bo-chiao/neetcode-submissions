class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Binary search to find the correct row
        left, right = 0, len(matrix) - 1
        while left <= right:
            mid = (left + right) // 2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                # Binary search within the row
                colLeft, colRight = 0, len(matrix[mid]) - 1
                while colLeft <= colRight:
                    colMid = (colLeft + colRight) // 2
                    if matrix[mid][colMid] == target:
                        return True
                    elif matrix[mid][colMid] < target:
                        colLeft = colMid + 1
                    else:
                        colRight = colMid - 1
                return False
            elif matrix[mid][0] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False
