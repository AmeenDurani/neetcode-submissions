class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = {}
        for c in t:
            need[c] = need.get(c, 0) + 1
        
        res = ""
        min_len = len(s) + 1
        
        window = {}
        have = 0
        required = len(need)
        l = 0


        for r, c in enumerate(s):
            window[c] = window.get(c, 0) + 1
            if c in need and window[c] == need[c]:
                have += 1
            
            while have == required:
                if r - l + 1 < min_len:
                    res = s[l: r + 1]
                    min_len = r - l + 1

                c = s[l]
                window[c] -= 1
                if c in need and window[c] < need[c]:
                    have -= 1

                l += 1

        return res
