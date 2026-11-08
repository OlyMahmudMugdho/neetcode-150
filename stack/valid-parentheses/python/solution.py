from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        pdict = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }

        for p in s:
            if p == '(' or p =='{' or p == '[':
                stack.append(p)
            else:
                if len(stack) > 0  and stack[-1] == pdict[p]:
                    stack.pop()
                else:
                    stack.append(p)

        return len(stack) == 0