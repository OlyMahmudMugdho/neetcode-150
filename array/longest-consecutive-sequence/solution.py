from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)

        longest = 0

        for num in nums_set:
            current_longest = 0
            if (num-1) in nums_set:
                continue

            else:
                current_longest += 1
                current_num = num
                while (current_num+1) in nums_set:
                    current_longest += 1
                    current_num += 1

            longest = max(longest, current_longest)

        return longest
