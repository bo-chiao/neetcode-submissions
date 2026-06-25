class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        t_count = {}
        for c in t:
            t_count[c] = t_count.get(c, 0) + 1
        required = len(t_count)

        ans = (float("inf"), 0, 0)
        l = 0
        window_count = {}
        
        for r in range(len(s)):
            char = s[r]
            window_count[char] = window_count.get(char, 0) + 1
            
            if char in t_count and window_count[char] == t_count[char]:
                required -= 1
            
            while required == 0:
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)
                
                removed_char = s[l]
                window_count[removed_char] -= 1
                
                if removed_char in t_count and window_count[removed_char] < t_count[removed_char]:
                    required += 1
                
                l += 1

        return "" if ans[0] == float("inf") else s[ans[1]:ans[2] + 1]