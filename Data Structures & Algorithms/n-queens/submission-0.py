class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def newQueenIsValid(board: List[List[str]], row, col):
            for i in range(row):
                for j in range(n):
                    if board[i][j] != 'Q':
                        continue
                    if j == col:
                        return False
                    if abs(row - i) == abs(col - j):
                        return False
            
            return True
                        

        results = []
        path = [['.'] * n for _ in range(n)]
        
        def backtrack(r, path):
            if r == n:
                results.append(["".join(row) for row in path])
                return

            for i in range(n):
                path[r][i] = 'Q'
                
                if newQueenIsValid(path, r, i):
                    backtrack(r + 1, path)

                path[r][i] = '.'
        
        backtrack(0, path)

        return results
