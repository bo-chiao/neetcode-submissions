"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        heap = []
        room_needed = 0

        intervals.sort(key=lambda x: x.start)

        for interval in intervals:
            while heap and interval.start >= heap[0]:
                heapq.heappop(heap)

            heapq.heappush(heap, interval.end)

            room_needed = max(len(heap), room_needed)
        
        return room_needed
