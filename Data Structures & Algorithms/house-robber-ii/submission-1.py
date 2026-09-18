class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def rob_i(start, end):
            two_back, one_back = 0, 0
            for i in range(start, end):
                num = nums[i]
                curr = max(num + two_back, one_back)
                two_back, one_back = one_back, curr

            return one_back

        return max(rob_i(0, len(nums) - 1), rob_i(1, len(nums)))
