class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = len(s)
        last = l - 1
        first = 0
        s = s.lower()

        while first < last:
            while not s[first].isalnum():
                first += 1
                if first == l:
                    return True
            while not s[last].isalnum():
                last -= 1
                if last == 0:
                    return True
            
            if s[first] != s[last]:
                return False
            
            first += 1
            last -= 1
        return True
            

        