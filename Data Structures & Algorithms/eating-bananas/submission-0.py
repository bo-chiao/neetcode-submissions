class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        ans = float("inf")

        while l <= r:
            i = (l + r) // 2
            time_sum = 0
            for pile in piles:
                time_sum += math.ceil(pile / i)

            if time_sum <= h:
                ans = min(ans, i)
                r = i - 1
            else:
                l = i + 1
        
        return ans
