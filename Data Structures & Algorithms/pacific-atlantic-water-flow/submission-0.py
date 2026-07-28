class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])

        pacific_reachable = set()
        atlantic_reachable = set()

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def dfs(r, c, prev_height, ocean):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or heights[r][c] < prev_height:
                return

            if (r, c) in ocean:
                return

            ocean.add((r, c))

            for dr, dc in directions:
                dfs(r + dr, c + dc, heights[r][c], ocean)
            

        for r in range(ROWS):
            dfs(r, 0, -1, pacific_reachable)
            dfs(r, COLS - 1, -1, atlantic_reachable)

        for c in range(COLS):
            dfs(0, c, -1, pacific_reachable)
            dfs(ROWS - 1, c, -1, atlantic_reachable)

        return list(pacific_reachable & atlantic_reachable)
