class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False
        
        count_1 = [0 for _ in range(26)]
        count_2 = [0 for _ in range(26)]

        for letter in s1:
            count_1[ord(letter) - ord("a")] += 1

        l = 0
        for r in range(len(s2)):
            count_2[ord(s2[r]) - ord("a")] += 1

            if r >= len(s1):
                count_2[ord(s2[l]) - ord("a")] -= 1
                l += 1
            
            if count_1 == count_2:
                return True

        return False
