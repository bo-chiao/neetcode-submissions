class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-1 * weight for weight in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            heaviest = -1 * heapq.heappop(heap)
            second_heaviest = -1 * heapq.heappop(heap)

            if heaviest != second_heaviest:
                remaining = heaviest - second_heaviest
                heapq.heappush(heap, -1 * remaining)

        return -1 * heap[0] if heap else 0
        