class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_count = Counter(t)

        ans = [float("inf"), 0, 0]
        required = len(t_count)
        s_count = {}

        l = 0
        for r in range(len(s)):
            s_count[s[r]] = s_count.get(s[r], 0) + 1
            
            if s[r] in t_count and s_count[s[r]] == t_count[s[r]]:
                required -= 1

            while required == 0:
                if r - l + 1 < ans[0]:
                    ans[0] = r - l + 1
                    ans[1] = l
                    ans[2] = r

                s_count[s[l]] -= 1

                if s[l] in t_count and s_count[s[l]] < t_count[s[l]]:
                    required += 1
                    
                l += 1

        return "" if ans[0] == float("inf") else s[ans[1]:ans[2] + 1]
