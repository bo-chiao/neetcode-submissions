class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        
        seq_len = {}
        for num in nums_set:
            if num - 1 not in nums_set:
                seq_len[num] = 0

        max_seq_len = 0
        for num in seq_len:
            count = 1
            while True:
                if num + 1 in nums_set:
                    count += 1
                    num += 1
                else:
                    break
            max_seq_len = max(max_seq_len, count)
        
        return max_seq_len
