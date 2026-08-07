class Solution:
    def toDict(self, s: str) -> dict:
        s_d = {}
        for i in s:
            if i not in s_d:
                s_d[i] = 1
            else:
                s_d[i] += 1
        return s_d

    def isAnagram(self, s: str, t: str) -> bool:
        s_d, t_d = {}, {}

        if len(s) != len(t):
            return False

        return self.toDict(s) == self.toDict(t)      