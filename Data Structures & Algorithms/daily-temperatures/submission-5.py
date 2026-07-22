class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n

        unresolved_days = []

        for current_day, current_temp in enumerate(temperatures):
            while unresolved_days and current_temp > temperatures[unresolved_days[-1]]:
                prev_day = unresolved_days.pop()
                result[prev_day] = current_day - prev_day

            unresolved_days.append(current_day)

        return result
        