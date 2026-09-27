class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expansion(left, right) -> str:
            while left >= 0 and right <= len(s) - 1 and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1 : right]
        
        longest = ""
        for i in range(len(s)):
            odd = expansion(i, i)
            even = expansion(i, i + 1)

            candidate = even if len(even) > len(odd) else odd
            
            if len(candidate) > len(longest):
                longest = candidate
        
        return longest



        