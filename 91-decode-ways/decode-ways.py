class Solution:
    def numDecodings(self, s: str) -> int:
        
        """[1-9] --> 1
        0 & [1, 2] --> 1 or False, [1-9] --> prev, [10-26] --> +2nd_prev"""

        ans = [0]*(len(s)+1)
        if(s[0]=='0'):
            return 0
        ans[0]=1
        ans[1]=1
        for i in range(1, len(s)):
            ind = i+1
            if(s[i]!='0'):
                ans[ind]=ans[ind-1]
                if('10'<=s[i-1:i+1]<='26'):
                    ans[ind]+=ans[ind-2]
            else:
                if(s[i-1] not in ['1', '2']):
                    return 0
                else:
                    ans[ind] = ans[ind-2]
        #print(ans)
        return ans[-1]
