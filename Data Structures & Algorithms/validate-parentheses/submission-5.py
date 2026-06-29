class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        p_map = {
            "(" : ")",
            "{" : "}",
            "[" : "]"
        }
        
        for p in s:
            if p in p_map:
                stack.append(p)
            else:
                if len(stack) == 0 or p != p_map[stack.pop()]:
                    return False
        
        return len(stack) == 0
