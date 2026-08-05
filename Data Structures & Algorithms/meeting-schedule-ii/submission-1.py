"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        room_needed = 0
        heap = []

        intervals.sort(key=lambda x: x.start)
        for interval in intervals:
            while heap and heap[0] <= interval.start:
                heapq.heappop(heap)
            
            heapq.heappush(heap, interval.end)
            room_needed = max(len(heap), room_needed)

        return room_needed
        