class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0

        count = defaultdict(int)
        duplicates = 0

        l, r = 0, 0

        while r < len(s):
            count[s[r]] += 1
            if count[s[r]] > 1:
                duplicates += 1

            while duplicates > 0:
                count[s[l]] -= 1
                if count[s[l]] == 1:
                    duplicates -= 1
                l += 1

            max_len = max(r - l + 1, max_len)
            r += 1

        return max_len
        