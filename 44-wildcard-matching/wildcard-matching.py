class Solution:
    def isMatch(self, s: str, p: str) -> bool:
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