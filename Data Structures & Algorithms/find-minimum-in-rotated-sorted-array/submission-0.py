class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        
        while l <= r:
            i = (l + r) // 2
            num_l, num_r, num = nums[l], nums[r], nums[i]

            if num < num_r:
                r = i
            else:
                l = i + 1

        return num
