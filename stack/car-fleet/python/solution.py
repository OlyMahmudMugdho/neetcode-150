class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        stack = []

        for pos, spd in cars:
            t = (target - pos) / spd

            if not stack or t > stack[-1]:
                stack.append(t)


        return len(stack)