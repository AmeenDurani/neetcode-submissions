class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        se = set()

        l, r = 0, 0

        while r < len(s):
            while s[r] in se:
                se.remove(s[l])
                l += 1
            se.add(s[r])

            res = max(res, r - l + 1)
            r += 1
        return res
        