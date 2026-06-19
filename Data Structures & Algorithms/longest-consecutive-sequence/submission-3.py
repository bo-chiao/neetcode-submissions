class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_seq_len = 0
        for num in nums_set:
            if num - 1 not in nums_set:
                current_num = num
                current_len = 1
                
                while True:
                    if num + 1 in nums_set:
                        num += 1
                        current_len += 1
                    else:
                        break
                max_seq_len = max(max_seq_len, current_len)
        
        return max_seq_len