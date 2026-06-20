class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max_capacity = 0
        while l < r:
            h_l, h_r = heights[l], heights[r]
            max_capacity = max(max_capacity, (r - l) * min(h_l, h_r))
            if h_l >= h_r:
                r -= 1
            else:
                l += 1
        return max_capacity
