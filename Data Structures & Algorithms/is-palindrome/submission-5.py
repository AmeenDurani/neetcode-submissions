class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = len(s)
        last = l - 1
        first = 0
        s = s.lower()

        while first < last:
            while (not s[first].isalnum()) and (first < l -1):
                first += 1
            while (not s[last].isalnum()) and (last > 0):
                last -= 1
            
            if s[first].isalnum() and s[last].isalnum() and s[first] != s[last]:
                return False
            
            first += 1
            last -= 1
        return True
            

        