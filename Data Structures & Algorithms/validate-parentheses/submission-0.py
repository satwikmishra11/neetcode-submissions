class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_map = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in bracket_map:
                # Closing bracket
                if not stack or stack[-1] != bracket_map[char]:
                    return False
                stack.pop()
            else:
                # Opening bracket
                stack.append(char)
        
        return len(stack) == 0
            