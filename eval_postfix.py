class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Leetcode's 150. Evaluate Reverse Polish Notation
        
        ops = {"+": lambda x,y: y+x, "-": lambda x,y: y-x, "*": lambda x,y: y*x, "/": lambda x,y: int(y/x)}
        
        def evaluate(curr):
            if curr in ops:
                op = ops[curr]
                return op(evaluate(tokens.pop()), evaluate(tokens.pop()))
            else:
                return int(curr)
            
        return evaluate(tokens.pop())
