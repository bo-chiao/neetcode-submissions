class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            i = (l + r) // 2

            if nums[i] == target:
                return i

            if nums[l] <= nums[i]:
                if nums[l] <= target < nums[i]:
                    r = i - 1
                else:
                    l = i + 1
            else:
                if nums[i] < target <= nums[r]:
                    l = i + 1
                else:
                    r = i - 1

        return -1
