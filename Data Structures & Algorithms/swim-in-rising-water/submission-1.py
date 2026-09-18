class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        side = len(grid)
        
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

        heap = [(grid[0][0], (0, 0))]
        visited = set()

        while heap:
            time, (r, c) = heapq.heappop(heap)

            if (r, c) in visited:
                continue

            if (r, c) == (side - 1, side - 1):
                return time

            visited.add((r, c))

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (nr < 0 or nc < 0 or nr >= side or nc >= side or (nr, nc) in visited):
                    continue 

                heapq.heappush(heap, (max(time, grid[nr][nc]), (nr, nc)))
        