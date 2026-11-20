class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hset = set()

        left = 0
        right = 0
        max_length = 0

        while right < len(s):
            if s[right] not in hset:
                hset.add(s[right])
                max_length = max(max_length, (right - left))
                right += 1

            else:
                right += 1

                