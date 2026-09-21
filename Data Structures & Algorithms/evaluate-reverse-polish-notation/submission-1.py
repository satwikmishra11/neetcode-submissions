class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
    
        for token in tokens:
            if token in {"+", "-", "*", "/"}:
                b = stack.pop()  # second operand
                a = stack.pop()  # first operand
                
                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                else:  # division
                    # Truncate toward zero
                    stack.append(int(a / b))
            else:
                stack.append(int(token))
        
        return stack[-1]

            