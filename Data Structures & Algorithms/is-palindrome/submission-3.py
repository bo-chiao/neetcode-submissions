class Solution:
    def isPalindrome(self, s: str) -> bool:
        head, tail = 0, len(s) - 1

        def elementType(word: str) -> int:
            idx = ord(word)
            if (ord("a") <= idx <= ord("z")) or (ord("0") <= idx <= ord("9")):
                return idx
            elif ord("A") <= idx <= ord("Z"):
                return idx + 32
            else:
                return -1

        while head < tail:
            if elementType(s[head]) == -1:
                head += 1
                continue
            if elementType(s[tail]) == -1:
                tail -= 1
                continue
            if elementType(s[head]) != elementType(s[tail]):
                return False

            head += 1
            tail -= 1
        return True
