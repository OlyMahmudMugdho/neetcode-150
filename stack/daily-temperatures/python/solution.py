from collections import deque


class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack = deque()
        res = [0] * len(temperatures)

        i = 0

        while (i < len(temperatures)):
            while( (len(stack) != 0) and (temperatures[stack[-1]] < temperatures[i]) ):
                j = stack.pop()
                res[j] = i - j

            stack.append(i)

            i += 1
        
        return res


s = Solution()

print(s.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))