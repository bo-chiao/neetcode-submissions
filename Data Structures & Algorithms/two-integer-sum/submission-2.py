class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx_map = {}
        for idx, num in enumerate(nums):
            diff = target - num
            if diff in idx_map:
                return [idx_map[diff], idx]
            else:
                idx_map[num] = idx
                
