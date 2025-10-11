class Solution:
    def calculate(self, s: str) -> int:
        s = '0+'+s

        stack = []
        st = ''
        local_s = []
        for e in s:
            if(e == ' ' and st):
                if(st and st != ' '):
                    st = int(st)
                    local_s.append(st)
                st = ''
            elif(e == '+' or e == '-'):
                if(st and st != ' '):
                    st = int(st)
                    local_s.append(st)
                    st = ''
                local_s.append(e)
            elif(e == '('):
                stack.append(local_s)
                local_s = []
                st = ''
            elif(e == ')'):
                if(st and st!=' '):
                    local_s.append(int(st))
                ans = 0
                while(local_s):
                    num = local_s.pop()
                    op = local_s.pop() if local_s else '+'
                    if(op=='+'):
                        ans+=num
                    if(op=='-'):
                        ans += (-num)
                local_s.append(ans)
                stack[-1]+=local_s
                local_s = stack.pop()
                st = ''
            else:
                st+=e
            
            #print(stack, local_s, st)


        if(st and st!=' '):
            local_s.append(int(st))
        
        if(local_s):
            ans = 0
            while(local_s):
                num = local_s.pop()
                op = local_s.pop() if local_s else '+'
                if(op=='+'):
                    ans+=num
                if(op=='-'):
                    ans += (-num)
        return ans


