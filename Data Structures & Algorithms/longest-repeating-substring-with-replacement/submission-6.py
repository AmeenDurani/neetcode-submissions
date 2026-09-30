class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d = {}
        res = 0
        l, r = 0, 0

        while r < len(s):
            d[s[r]] = d.get(s[r], 0) + 1

            while (r - l + 1) - max(d.values()) > k:
                d[s[l]] = d.get(s[l], 1) - 1
                l += 1
            
            res = max(res, r - l + 1)
            r += 1
        
        return res
