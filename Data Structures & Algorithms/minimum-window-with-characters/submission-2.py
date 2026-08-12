class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = ""
        left_ptr = 0
        
        need = {}
        need_n = 0
        for c in t:
            if c not in need:
                need_n += 1
            need[c] = 1 + need.get(c, 0)

        have = {}
        have_n = 0
        for right_ptr, right_char in enumerate(s):
            have[right_char] = 1 + have.get(right_char, 0)
            
            if right_char in need and \
               have[right_char] == need[right_char]:
               have_n += 1

            while have_n == need_n:
                if len(res) > right_ptr - left_ptr + 1 or \
                   res == "":
                   res = s[left_ptr : right_ptr + 1]


                left_char = s[left_ptr]
                have[left_char] -= 1

                if left_char in need and \
                   have[left_char] < need[left_char]:
                   have_n -= 1
                
                left_ptr += 1
        return res    
