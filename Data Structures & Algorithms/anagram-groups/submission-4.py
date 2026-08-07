class Solution:
    def toTuple(self, s: str) -> tuple:
        count = [0] * 26
        for c in s:
            count[ord(c)-ord('a')] += 1
        return tuple(count)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        res = []
        for s in strs:
            t = self.toTuple(s)
            if t not in d:
                l = len(res)
                d[t] = l
                res.append([s])
            else:
                res[d[t]].append(s)
        return res
        