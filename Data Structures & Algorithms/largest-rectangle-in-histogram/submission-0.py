class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        prefix, suffix = [-1] * n, [n] * n

        stack = []
        for i in range(n):
            while stack and heights[i] < heights[stack[-1]]:
                l = stack.pop()
                suffix[l] = i
            
            stack.append(i)

        stack = []
        for i in range(n - 1, -1, -1):
            while stack and heights[i] < heights[stack[-1]]:
                r = stack.pop()
                prefix[r] = i

            stack.append(i)

        max_area = 0
        for i in range(n):
            area = heights[i] * (suffix[i] - prefix[i] - 1)
            max_area = max(max_area, area)

        return max_area
        