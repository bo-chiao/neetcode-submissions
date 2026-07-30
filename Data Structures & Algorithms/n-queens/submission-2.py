class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        results = []
        board = [["."] * n for _ in range(n)]

        col = set()
        pos_diag = set()
        neg_diag = set()

        def backtrack(r):
            if r >= n:
                results.append(["".join(row) for row in board])
                return

            for c in range(n):
                if c in col or r + c in pos_diag or r - c in neg_diag:
                    continue

                board[r][c] = "Q"
                col.add(c)
                pos_diag.add(r + c)
                neg_diag.add(r - c)

                backtrack(r + 1)
        
                board[r][c] = "."
                col.remove(c)
                pos_diag.remove(r + c)
                neg_diag.remove(r - c)

        backtrack(0)
        return results
