class Solution:
    def numDecodings(self, s: str) -> int:
        ans = [0]*(len(s))
        if(s[0]=='0'):
            return 0
        ans[0]=1
        for i in range(1, len(s)):
            if(s[i]!='0'):
                ans[i]=ans[i-1]
                if('10'<=s[i-1:i+1]<='26'):
                    if(i-2>=0):
                        ans[i]+=ans[i-2]
                    else:
                        ans[i]+=1
            else:
                if(s[i-1] not in ['1', '2']):
                    return 0
                else:
                    if(i-2>=0):
                        ans[i]+=ans[i-2]
                    else:
                        ans[i]+=1
        #print(ans)
        return ans[-1]
