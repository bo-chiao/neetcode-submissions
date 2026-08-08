class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        p_map = {
            "[": "]",
            "{": "}",
            "(": ")"
        }

        for p in s:
            if p in p_map:
                stack.append(p)
            else:
                if len(stack) == 0:
                    return False
                    
                left = stack.pop()
                if p != p_map[left]:
                    return False

        return len(stack) == 0
        