class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])

        def backtrack(r, c, k):
            if k == len(word):
                return True

            if r < 0 or c < 0 or r >= ROWS or c >= COLS:
                return False

            if board[r][c] != word[k]:
                return False

            temp = board[r][c]
            board[r][c] = "#"

            isValid = backtrack(r + 1, c, k + 1) or backtrack(r, c + 1, k + 1) or backtrack(r - 1, c, k + 1) or backtrack(r, c - 1, k + 1)

            board[r][c] = temp

            return isValid
        
        for i in range(ROWS):
            for j in range(COLS):
                if backtrack(i, j, 0):
                    return True

        return False
