class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        remove_count = 0

        intervals.sort(key=lambda x: x[1])
        prev_end = -50001
        
        for start, end in intervals:
            if start >= prev_end:
                prev_end = end
            else:
                remove_count += 1
                
        return remove_count
        