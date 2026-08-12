class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, res = 0, 0
        unique = set()

        for right, val in enumerate(s):
            while val in unique:
                unique.remove(s[left])
                left += 1

            unique.add(val)
            res = max(right - left + 1, res)
        
        return res
