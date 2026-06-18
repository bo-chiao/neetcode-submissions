class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for idx, num in enumerate(nums):
            residual = target - num
            if residual in hashmap:
                return [hashmap[residual], idx]
            hashmap[num] = idx