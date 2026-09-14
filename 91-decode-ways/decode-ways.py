class Solution:
    def numDecodings(self, s: str) -> int:
        if(s[0] == '0'):
            return 0
        
        is_feasible = True
        dp = {}
        def count(ind):
            if(ind in dp):
                return dp[ind]
            nonlocal is_feasible
            if(ind==0):
                return 1
            if(ind == 1):
                num = int(s[:2])
                if(s[ind]=='0'):
                    if(num == 10 or num == 20):
                        return 1
                    else:
                        is_feasible = False
                else:
                    if(11<=num<=26):
                        return 2
                    else:
                        return 1
            
            ans = 0
            num = int(s[ind-1:ind+1])
            if(s[ind]=='0'):
                if(num == 10 or num == 20):
                    ans += count(ind-2)
                else:
                    is_feasible = False
            else:
                ans += count(ind-1)
                if(11<=num<=26):
                    ans += count(ind-2)
            dp[ind] = ans
            return ans
            
        ans = count(len(s)-1)
        if(is_feasible == False):
            return 0
        return ans