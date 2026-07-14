class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for point in points:
            x, y = point

            dist_sq = x ** 2 + y ** 2
            
            heapq.heappush(heap, (-dist_sq, point))

            if len(heap) > k:
                heapq.heappop(heap)

        return  [point for dist, point in heap]
