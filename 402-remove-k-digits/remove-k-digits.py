class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if(k==len(num)):
            return "0"

        stack = []
        for ch in num:
            is_broken = False
            while(stack and k>0 and stack[-1]>ch):
                x = stack.pop()
                if(x!="0"):
                    k-=1
            stack.append(ch)

        #print(stack, k)
        while(stack and k>0):
            stack.pop()
            k-=1
        ans = ""
        for ch in stack:
            if(not ans and ch=="0"):
                pass
            else:
                ans+=ch
        return ans if ans else "0"
