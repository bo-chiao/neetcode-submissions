class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def save(r, c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or board[r][c] != "O":
                return

            board[r][c] = "T"

            for dr, dc in directions:
                save(r + dr, c + dc)

        for r in range(ROWS):
            save(r, 0)
            save(r, COLS - 1)

        for c in range(COLS):
            save(0, c)
            save(ROWS - 1, c)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"
        