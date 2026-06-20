class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l_max = [0 for _ in range(n)]
        r_max = [0 for _ in range(n)]

        for i in range(1, n - 1):
            l_max[i] = max(l_max[i - 1], height[i - 1])
            r_max[n - i - 1] = max(r_max[n - i], height[n - i])
        
        area = 0
        for i in range(1, n - 1):
            area += max(0, min(l_max[i], r_max[i]) - height[i])

        return area
