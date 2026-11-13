from collections import deque


class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = deque()
        operations = {'+', '-', '*', '/'}

        for token in tokens:
            if token not in operations:
                stack.append(int(token))
            else:
                if token == '+':
                    b = stack.pop()
                    a = stack.pop()

                    res = a + b

                    stack.append(res)

                elif token == '-':
                    b = stack.pop()
                    a = stack.pop()

                    res = a - b

                    stack.append(res)

                elif token == '*':
                    b = stack.pop()
                    a = stack.pop()

                    res = a * b

                    stack.append(res)

                elif token == '/':
                    b = stack.pop()
                    a = stack.pop()

                    res = a / b

                    stack.append(int(res))

        return int(stack[-1])


s = Solution()
print(s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
))