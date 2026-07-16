class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = []
        queue = deque([0] * n)

        task_count = Counter(tasks)

        for _, count in task_count.items():
            heapq.heappush(heap, -1 * count)

        time = 0

        while heap or any(queue):
            if heap:
                count = heapq.heappop(heap)
                count += 1
            else:
                count = 0

            queue.append(count)

            cooldowned_task = queue.popleft()
            if cooldowned_task != 0:
                heapq.heappush(heap, cooldowned_task)

            time += 1

        return time
        