class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        l, r, freq_c, res = 0, 0, 0, 0

        d = {}

        while r < len(s):
            d[s[r]] = d.get(s[r], 0) + 1
            freq_c = max(freq_c, d[s[r]])

            while (r - l + 1) - freq_c > k:
                d[s[l]] = d.get(s[l], 1) - 1
                l += 1
            
            res = max(res, r - l + 1)
            r += 1
        return res
