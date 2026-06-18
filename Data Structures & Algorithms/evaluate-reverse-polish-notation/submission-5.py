class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i == '+':
                val_2 = stack.pop()
                val_1 = stack.pop()
                stack.append(val_1 + val_2)
            elif i == '-':
                val_2 = stack.pop()
                val_1 = stack.pop()
                stack.append(val_1 - val_2)
            elif i == '*':
                val_2 = stack.pop()
                val_1 = stack.pop()
                stack.append(val_1 * val_2)
            elif i == '/':
                val_2 = stack.pop()
                val_1 = stack.pop()
                stack.append(int(float(val_1) / val_2))
            else:
                stack.append(int(i))
        return stack.pop()