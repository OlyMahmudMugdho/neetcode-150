class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charset = set()

        length = 0
        ans = 0

        left = 0
        right = left

        while(right < len(s)):
            if s[right] not in charset:
                charset.add(s[right])
                length = right - left + 1
                ans = max(ans, length)
                right += 1

            else:
                charset.remove(s[left])
                left += 1

        return ans