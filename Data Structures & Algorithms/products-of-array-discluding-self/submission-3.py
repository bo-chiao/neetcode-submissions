class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1] * n
        suffix = [1] * n

        prefix_product, suffix_product = 1, 1
        for i in range(n):
            prefix[i] = prefix_product
            suffix[- i - 1] = suffix_product

            prefix_product *= nums[i]
            suffix_product *= nums[- i - 1]

        return [prefix[i] * suffix[i] for i in range(n)]
