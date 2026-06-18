class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, suffix = [], []
        prod_prefix, prod_suffix = 1, 1
        n = len(nums)
        for i in range(n):
            prod_prefix *= nums[i]
            prefix.append(prod_prefix)
            
            prod_suffix *= nums[n-i-1]
            suffix.append(prod_suffix)
        
        res = []
        for i in range(n):
            if i == 0:
                product = suffix[n-i-2]
            elif i == n-1:
                product = prefix[i-1]
            else:
                product = prefix[i-1] * suffix[n-i-2]
            res.append(product)
        return res
            
