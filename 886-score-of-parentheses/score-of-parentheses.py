class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []

        for i, e in enumerate(s):
            if(e == '('):
                stack.append('(')
            else:
                if(stack[-1]=='('):
                    stack.pop()
                    stack.append(1)
                else:
                    count = 0
                    while(stack[-1]!='('):
                        count += stack.pop()
                    stack.pop()
                    stack.append(2*count)
                    
        ans = sum(stack)
        return ans