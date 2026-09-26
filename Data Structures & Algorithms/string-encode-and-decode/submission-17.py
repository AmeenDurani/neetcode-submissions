class Solution:

    def encode(self, strs: List[str]) -> str:
        # example, given ['abc', 'defg'], we do "3-abc4-defg"
        res = ""
        for s in strs:
            res += str(len(s)) + "-" + s
        return res

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            # obtain count of string
            count = ""
            while s[i] != "-":
                count += s[i]
                i += 1
            i += 1
            count = int(count)
            
            res.append(s[i : i + count])
            i += count
        return res
