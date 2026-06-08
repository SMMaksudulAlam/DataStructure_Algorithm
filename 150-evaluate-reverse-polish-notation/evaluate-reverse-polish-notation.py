class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for e in tokens:
            #print(stack, e)
            if(e in ["+", "-", "*", "/"]):
                if(e == "+"):
                    op1 = stack.pop()
                    op2 = stack.pop()
                    stack.append(op1+op2)
                if(e == "-"):
                    op1 = stack.pop()
                    op2 = stack.pop()
                    stack.append(op2-op1)
                if(e == "*"):
                    op1 = stack.pop()
                    op2 = stack.pop()
                    stack.append(op1*op2)
                if(e == "/"):
                    op1 = stack.pop()
                    op2 = stack.pop()
                    ans = (op2*1.0)/op1
                    if(ans>=0):  
                        stack.append(math.floor(ans))
                    else:
                        stack.append(math.ceil(ans))
            else:
                stack.append(int(e))

        return stack[-1]