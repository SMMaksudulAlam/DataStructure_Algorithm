class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        s_ = ""
        for e in s:
            if(e=='['):
                stack.append(s_)
                s_ = ""
            elif(e==']'):
                last = stack.pop()
                x = len(last)-1
                while(x>=0 and '0'<=last[x]<='9'):
                    x-=1
                num = int(last[x+1:])
                post = s_*num
                pre = last[:x+1]
                total = pre+post
                s_ = total
            else:
                s_+=e
        ans = s_
        return ans