class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pair = {}
        for idx, num in enumerate(nums):
            if (target - num) in pair:
                return [pair[target - num], idx]
            else:
                pair[num] = idx if num not in pair else pair[num]
        return []