class Solution:
    def isValid(self, s: str) -> bool:
        test = { 
                ")":"(",
                "}":"{",
                "]":"["
               }
        stack = []
        for c in s:
            if c not in test:
                stack.append(c)
                continue
            if stack and test[c] == stack[-1]:
                stack.pop()
                continue
            return False
        if not stack:
            return True
        return False
            
            