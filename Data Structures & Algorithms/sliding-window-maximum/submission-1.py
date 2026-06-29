class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        q = deque(maxlen=n)
        result = []

        l = 0
        for r in range(n):
            while q and q[0] < l:
                q.popleft()
            
            while q and nums[q[-1]] < nums[r]:
                q.pop()

            q.append(r)

            if r >= k - 1:
                result.append(nums[q[0]])
                l += 1

        return result
