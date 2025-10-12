class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if(not s or s == s[::-1]):
            return s
        
        ind = 0
        for i in range(len(s)//2+1):
            s_ = s[:i+1]
            s_ = s_[::-1]
            ln = len(s_)
            if(s[i:i+ln] == s_):
                ind = max(ind, i+ln)
            if(s[i+1:i+1+ln] == s_):
                ind = max(ind, i+1+ln)
        
        s = s[ind:][::-1]+s
        return s
