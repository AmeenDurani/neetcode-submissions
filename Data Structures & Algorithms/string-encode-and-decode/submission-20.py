class Solution:

    def encode(self, strs: List[str]) -> str:
        r = ""
        for s in strs:
            r += str(len(s)) + "_" + s
        
        return r

    def decode(self, s: str) -> List[str]:
        r = []
        p = 0

        while p < len(s):
            num_len = 0
            while s[p + num_len] != "_":
                num_len += 1
            num = int(s[p : p + num_len])
            p += num_len + 1

            r.append(s[p : p + num])
            p += num
        
        return r


