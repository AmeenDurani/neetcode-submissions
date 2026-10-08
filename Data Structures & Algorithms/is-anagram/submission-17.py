class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        x = {}
        for c in s:
            x[c] = x.get(c, 0) + 1
        
        y = {}
        for c in t:
            y[c] = y.get(c, 0) + 1
        
        return x == y
        