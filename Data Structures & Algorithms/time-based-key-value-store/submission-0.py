class TimeMap:

    def __init__(self):
        self.time_map = {}


    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.time_map:
            self.time_map[key] = []

        self.time_map[key].append((timestamp, value))


    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time_map:
            return ""

        values = self.time_map[key]
        if timestamp < values[0][0]:
            return ""
        
        l, r = 0, len(values) - 1
        
        while l <= r:
            i = (l + r) // 2
            
            if values[i][0] == timestamp:
                return values[i][1]
            elif values[i][0] < timestamp:
                l = i + 1
            else:
                r = i - 1
        
        return values[r][1]
