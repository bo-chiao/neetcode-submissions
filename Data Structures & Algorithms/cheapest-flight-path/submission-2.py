class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        airports = {}
        for i in range(n):
            airports[i] = {}

        for from_i, to_i, price_i in flights:
            airports[from_i][to_i] = price_i

        memo = {}

        def dfs(city, flights_left):
            if city == dst:
                return 0

            if flights_left == 0:
                return float("inf")

            if (city, flights_left) in memo:
                return memo[(city, flights_left)]

            min_price = float("inf")
            for next_i, price_i in airports[city].items():
                min_price = min(price_i + dfs(next_i, flights_left - 1), min_price)

            memo[(city, flights_left)] = min_price

            return min_price

        min_cost = dfs(src, k + 1)

        return min_cost if min_cost != float("inf") else -1
