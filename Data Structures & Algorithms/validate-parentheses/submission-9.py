class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            "(" : ")",
            "{" : "}",
            "[" : "]"
        }
        
        stack = []

        for c in s:
            if c in pairs:
                stack.append(pairs[c])
                continue
            
            if not stack or stack[-1] != c:
                return False
            
            stack.pop(-1)
        
        return not stack
                
