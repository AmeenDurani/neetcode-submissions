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
                stack.insert(0, pairs[c])
                continue
            
            if not stack or stack[0] != c:
                return False
            
            stack.pop(0)
        
        return not stack
                
