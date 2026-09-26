class Solution:
    def isPalindrome(self, s: str) -> bool:
        alnum_string = "".join(c for c in s.lower() if c.isalnum())

        l, r = 0, len(alnum_string) - 1
        while l < r:
            if alnum_string[l] != alnum_string[r]: return False

            l += 1
            r -= 1

        return True
        
        