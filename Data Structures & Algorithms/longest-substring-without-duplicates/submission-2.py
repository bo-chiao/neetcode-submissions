class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        max_len = 0
        l = 0

        for r, char in enumerate(s):
            while char in chars:
                chars.remove(s[l])
                l += 1

            chars.add(char)
            max_len = max(r - l + 1, max_len)

        return max_len
