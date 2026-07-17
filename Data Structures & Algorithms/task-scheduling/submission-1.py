class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_counter = Counter(tasks)

        task_counts = [-1 * count for count in task_counter.values()]
        
        heapq.heapify(task_counts)

        cooldown_queue = deque([])

        time = 0
        while task_counts or cooldown_queue:
            time += 1

            if task_counts:
                count = heapq.heappop(task_counts) + 1
                
                if count != 0:
                    cooldown_queue.append((count, time + n))

            if cooldown_queue and cooldown_queue[0][1] == time:
                count, _ = cooldown_queue.popleft()
                heapq.heappush(task_counts, count)
        
        return time
