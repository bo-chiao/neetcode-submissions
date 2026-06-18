class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0] * len(temperatures)
        stack = []
        for idx, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                idx_0, _ = stack.pop()
                output[idx_0] = idx - idx_0
            stack.append((idx, temp))
        return output
