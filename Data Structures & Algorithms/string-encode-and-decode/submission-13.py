class Solution:
    separator = ">"

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            length = str(len(s))
            res.append(length + self.separator + s)

        return "".join(res)

    def separate(self, sep_index: int, s_len: int, s: str) -> str:
        if (sep_index + s_len) >= len(s): return ""
        return s[sep_index + 1 : sep_index + s_len + 1]

    def decode(self, s: str) -> List[str]:
        strs = []
        s_len = ""
        i, s_max = 0, len(s)

        while i < s_max:
            if s[i] == self.separator:
                i_len = int(s_len)
                strs.append(self.separate(i, i_len, s))
                i = i + i_len
                s_len = ""
            else:
                s_len += s[i]
            i += 1  
        return strs