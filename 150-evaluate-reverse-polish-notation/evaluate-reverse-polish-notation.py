class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for e in tokens:
            if(e not in ['+', '-', '*', '/']):
                stack.append(int(e))
            else:
                if(e=='+'):
                    e1 = stack.pop()
                    e2 = stack.pop()
                    stack.append(e2+e1)
                if(e=='-'):
                    e1 = stack.pop()
                    e2 = stack.pop()
                    stack.append(e2-e1)
                if(e=='*'):
                    e1 = stack.pop()
                    e2 = stack.pop()
                    stack.append(e2*e1)
                if(e=='/'):
                    e1 = stack.pop()
                    e2 = stack.pop()
                    div = e2/e1
                    if(div<0):
                        stack.append(ceil(div))
                    else:
                        stack.append(floor(div))
        
        return stack[-1]