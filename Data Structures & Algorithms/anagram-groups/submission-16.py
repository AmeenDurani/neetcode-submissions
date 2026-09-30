class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}

        for s in strs:
            s_s = tuple(sorted(s))

            if s_s in d:
                d[s_s].append(s)
            else:
                d[s_s] = [s]
        
        return list(d.values())

        