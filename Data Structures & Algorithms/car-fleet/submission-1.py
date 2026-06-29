class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time_buckets = [0.0] * target

        for i in range(len(position)):
            pos = position[i]
            time_buckets[pos] = (target - pos) / speed[i]

        fleet_count = 0
        max_time = 0

        for i in range(target - 1, -1, -1):            
            t = time_buckets[i]

            if t > 0 and t > max_time:
                fleet_count += 1
                max_time = t

        return fleet_count
