class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "-" + s
        return res

    def decode(self, s: str) -> List[str]:
        ptr = 0
        res = []

        while ptr < len(s):
            # read length
            # parse string
            offset = 0
            while s[ptr + offset] != "-":
                offset += 1
            
            num = int(s[ptr: ptr + offset])
            ptr += offset + 1
            part = s[ptr : ptr + num]
            ptr += num

            res.append(part)
        
        return res

