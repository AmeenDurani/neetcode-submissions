class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts = {}

        for c in s:
            counts[c] = counts.get(c, 0) + 1
        
        for c in t:
            counts[c] = counts.get(c, 0) - 1
        
        return not any(counts.values())
        