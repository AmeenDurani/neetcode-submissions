class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        d = {}
        for s in strs:
            st = tuple(sorted(s))
            if st not in d:
                d[st] = [s]
            else:
                d[st].append(s)
        
        return list(d.values())