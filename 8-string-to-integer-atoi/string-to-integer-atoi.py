class Solution:
    def myAtoi(self, s: str) -> int:
        ans = 0
        if(not s):
            return ans
        i = 0
        while(i<len(s) and s[i]==' '):
            i+=1
            
        neg = False
        if(i<len(s) and (s[i]=='-' or s[i]=='+')):
            if(s[i]=='-'):
                neg = True
            i+=1
        
        while(i<len(s)):
            if('0'<=s[i]<='9'):
                ans*=10
                ans+=int(s[i])
                i+=1
            else:
                break
        if(neg):
            ans*=-1

        if(ans>0):
            ans = min(2**31-1, ans)
        else:
            ans = max(-2**31, ans)
        return ans
