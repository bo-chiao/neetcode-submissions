class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            product = math.prod(nums[:i]) * math.prod(nums[i+1:])
            res.append(product)
        return res