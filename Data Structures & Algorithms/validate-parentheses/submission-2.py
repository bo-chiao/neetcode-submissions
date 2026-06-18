class Solution:
    def isValid(self, s: str) -> bool:
        parentheses_map = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        stack = []
        for i in s:
            if i in parentheses_map:
                if (not stack) or (stack[-1] != parentheses_map[i]):
                    return False
                else:
                    stack.pop()
            else:
                stack.append(i)
        if not stack:
            return True
        else: 
            return False
                