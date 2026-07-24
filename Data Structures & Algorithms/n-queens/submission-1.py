class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        results = []
        board = [["."] * n for _ in range(n)]

        cols = set()
        posDiag = set()
        negDiag = set()

        def backtrack(i):
            if i == n:
                results.append(["".join(row) for row in board])
                return

            for j in range(n):
                if (j in cols) or (i + j in posDiag) or (i - j in negDiag):
                    continue

                board[i][j] = "Q"
                cols.add(j)
                posDiag.add(i + j)
                negDiag.add(i - j)

                backtrack(i + 1)

                board[i][j] = "."
                cols.remove(j)
                posDiag.remove(i + j)
                negDiag.remove(i - j)

        backtrack(0)

        return results
