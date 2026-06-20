class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        idx_map = {}
        max_len = 0
        
        for i in range(len(s)):
            if s[i] in idx_map and idx_map[s[i]] >= l:
                l = idx_map[s[i]] + 1
            
            idx_map[s[i]] = i
            max_len = max(max_len, i - l + 1)
        
        return max_len
