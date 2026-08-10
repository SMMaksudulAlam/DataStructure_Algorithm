class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """
        dp = {}
        def match(ind1, ind2):
            if((ind1, ind2) in dp):
                return dp[(ind1, ind2)]
            if(ind1<0 or ind2<0):
                if(ind1<0 and ind2<0):
                    return True
                if(ind1<0 and "*"*(ind2+1) == p[:ind2+1]):
                    return True
                return False
            ans = False
            if(p[ind2] == '?' or p[ind2] == s[ind1]):
                ans = ans or match(ind1-1, ind2-1)
            elif(p[ind2] == '*'):
                ans = ans or match(ind1-1, ind2) or match(ind1, ind2-1)
            else:
                ans = False
            dp[(ind1, ind2)] = ans
            return dp[(ind1, ind2)]
        
        ans = match(len(s)-1, len(p)-1)
        return ans
        """

        lenS = len(s)
        lenP = len(p)

        dp = [[False]*(lenS+1) for _ in range(lenP+1)]
        dp[0][0] = True
        for i in range(1, lenP+1):
            if(p[i-1] == '*'):
                dp[i][0] = dp[i-1][0]

        for iP in range(1, lenP+1):
            for iS in range(1, lenS+1):
                if(p[iP-1] != "*"):
                    if(p[iP-1] == "?" or p[iP-1] == s[iS-1]):
                        dp[iP][iS] = dp[iP-1][iS-1]
                else:
                    dp[iP][iS] = dp[iP][iS-1] or dp[iP-1][iS]
        #print(dp)
        return dp[-1][-1]
        