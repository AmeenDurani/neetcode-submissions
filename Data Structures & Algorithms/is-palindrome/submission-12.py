class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        ss = "".join(c for c in s if c.isalnum())

        l, r = 0, len(ss) - 1

        while l < r:
            if ss[l] != ss[r]:
                return False
            
            l += 1
            r -= 1
        return True

        