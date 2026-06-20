class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums_sorted = sorted(nums)
        output = set()
        for i, num in enumerate(nums_sorted):
            target = -num
            l, r = i + 1, n - 1
            while l < r:
                if nums_sorted[l] + nums_sorted[r] == target:
                    output.add(tuple(sorted([nums_sorted[l], nums_sorted[r], num])))
                    l += 1
                    r -= 1
                elif nums_sorted[l] + nums_sorted[r] < target:
                    l += 1
                else:
                    r -= 1

        return list(output)
