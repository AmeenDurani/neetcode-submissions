class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        maxf = 0
        prev = 0
        for i, c in enumerate(s):
            count[c] = 1 + count.get(c, 0)
            maxf = max(maxf, count[c])

            while (i - prev + 1 - maxf) > k:
                count[s[prev]] -= 1
                prev += 1
            
            res = max(res, i - prev + 1)
        return res