class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0

        for subamount in range(1, amount + 1):
            for coin in coins:
                if subamount < coin:
                    continue

                dp[subamount] = min(1 + dp[subamount - coin], dp[subamount])

        return dp[amount] if dp[amount] != float("inf") else -1
