class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        l, r = 0, 1
        while r < len(prices):
            if prices[l] >= prices[r]:
                l = r
                r += 1
            else:
                if r == len(prices) - 1 or prices[r + 1] < prices[r]:
                    max_profit = max(max_profit, prices[r] - prices[l])
                r += 1

        return max_profit
