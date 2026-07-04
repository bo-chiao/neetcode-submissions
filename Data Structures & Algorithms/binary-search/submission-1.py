class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n - 1

        while l <= r:
            i = (l + r) // 2
            if nums[i] == target:
                return i
            elif nums[i] < target:
                l = i + 1
            else:
                r = i - 1

        return -1
        