class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        char_count = {}
        max_count = 0
        max_len = 0
        
        while r < len(s):
            char_count[s[r]] = char_count.get(s[r], 0) + 1
            max_count = max(char_count[s[r]], max_count)
            
            if (r - l + 1) - max_count > k:
                char_count[s[l]] -= 1
                l += 1
            
            max_len = max(r - l + 1, max_len)
            r += 1

        return max_len
