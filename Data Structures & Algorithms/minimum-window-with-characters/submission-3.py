class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target_char = Counter(t)
        remaining = len(target_char)
        
        l = 0
        min_len = float("inf")
        shortest_substring = ""

        for i in range(len(s)):
            if s[i] in target_char:
                target_char[s[i]] -= 1
                
                if target_char[s[i]] == 0:
                    remaining -= 1

            while remaining == 0:
                curr_len = i - l + 1
                if curr_len < min_len:
                    min_len = curr_len
                    shortest_substring = s[l:i+1]

                left_char = s[l]
                if left_char in target_char:
                    target_char[left_char] += 1
                    if target_char[left_char] > 0:
                        remaining += 1

                l += 1

        return shortest_substring

        