class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)

        target = Counter(s1)

        i = 0
        while n1 + i <= n2:
            window = Counter(s2[i : n1 + i])
            
            if target == window:
                return True

            i += 1

        return False
