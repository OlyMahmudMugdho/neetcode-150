class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1

        max_container = 0

        while left <= right:
            container_h = min(height[left], height[right])
            container_w = abs(left - right)

            area = container_h * container_w

            max_container = max(area, max_container)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_container
