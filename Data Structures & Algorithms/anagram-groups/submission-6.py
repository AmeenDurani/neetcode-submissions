class Solution:
    def toTuple(self, s: str) -> tuple:
        count = [0] * 26
        for c in s:
            count[ord(c)-ord('a')] += 1
        return tuple(count)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for s in strs:
            t = self.toTuple(s)
            if t not in d:
                d[t] = [s]
            else:
                d[t].append(s)
        return list(d.values())