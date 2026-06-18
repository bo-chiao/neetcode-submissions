class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        charCount = {}
        for char in s:
            if char in charCount:
                charCount[char] += 1
            else:
                charCount[char] = 1
        for char in t:
            if char not in charCount:
                return False
            if charCount[char] == 0:
                return False
            charCount[char] -= 1
        for i, v in charCount.items():
            if v > 0:
                return False
        return True