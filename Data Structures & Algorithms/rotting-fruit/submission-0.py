class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        queue = deque([])
        remaining = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    remaining += 1
                elif grid[r][c] == 2:
                    queue.append((r, c))

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        time = 0
        while queue and remaining > 0:
            for _ in range(len(queue)):
                r, c = queue.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS or grid[nr][nc] in (0, 2):
                        continue

                    grid[nr][nc] = 2
                    remaining -= 1

                    queue.append((nr, nc))

            time += 1

        return time if remaining == 0 else -1
