class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)

        target = Counter(s1)
        window = Counter(s2[:n1])

        for i in range(n1, n2):
            if target == window:
                return True
            
            left_char = s2[i - n1]
            window[left_char] -= 1

            if window[left_char] == 0:
                del window[left_char]

            curr_char = s2[i]
            window[curr_char] += 1

        return target == window
