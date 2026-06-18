class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s = {}
        count_t = {}
        
        for letter in s:
            count_s[letter] = count_s.get(letter, 0) + 1
        
        for letter in t:
            count_t[letter] = count_t.get(letter, 0) + 1

        return count_s == count_t