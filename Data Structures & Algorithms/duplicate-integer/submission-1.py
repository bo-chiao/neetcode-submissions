class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        :type nums: List[int]
        :rtype: bool
        """
        exist = set()
        for i in nums:
            if i in exist:
                return True
            else:
                exist.add(i)

        return False