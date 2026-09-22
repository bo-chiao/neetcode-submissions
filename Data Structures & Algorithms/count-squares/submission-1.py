class CountSquares:
    def __init__(self):
        self.freq = defaultdict(int)

    def add(self, point: List[int]) -> None:
        x, y = point
        self.freq[(x, y)] += 1

    def count(self, point: List[int]) -> int:
        squares = 0

        x1, y1 = point
        for x2, y2 in self.freq:
            if (
                x1 == x2
                or abs(x1 - x2) != abs(y1 - y2)
                or (x1, y2) not in self.freq
                or (x2, y1) not in self.freq
            ):
                continue

            squares += self.freq[(x2, y2)] * self.freq[(x1, y2)] * self.freq[(x2, y1)]

        return squares
