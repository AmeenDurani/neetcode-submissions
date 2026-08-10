class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_m = s.lower()
        for c in s:
            if not c.isalnum(): s_m = s_m.replace(c, "")
        return s_m == s_m[::-1]
        