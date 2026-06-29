class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {"+", "-", "*", "/"}

        for t in tokens:
            if t in operators:
                num2 = stack.pop()
                num1 = stack.pop()

                match t:
                    case "+":
                        stack.append(num1 + num2)
                    case "-":
                        stack.append(num1 - num2)
                    case "*":
                        stack.append(num1 * num2)
                    case "/":
                        stack.append(int(num1 / num2))
                    case _:
                        pass
            else:
                stack.append(int(t))

        return stack[-1]
