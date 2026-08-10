class Solution:
    def isPalindrome(self, s: str) -> bool:
        last = len(s) - 1
        first = 0
        s = s.lower()

        while first < last:
            while first < last and not s[first].isalnum():
                first += 1
            while first < last and not s[last].isalnum():
                last -= 1
            if s[first] != s[last]:
                return False
            
            first += 1
            last -= 1
        return True