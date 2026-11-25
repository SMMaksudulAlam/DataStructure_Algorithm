class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        left = 0
        for i, e in enumerate(s):
            if(e not in ['(', ')']):
                if(not stack):
                    stack.append(e)
                else:
                    stack[-1]+=e
            elif(e == '('):
                stack.append("")
            elif(e == ')'):
                s_ = stack.pop()
                if(not stack):
                    stack.append(s_[::-1])
                else:
                    stack[-1] += s_[::-1]
        return "".join(stack)