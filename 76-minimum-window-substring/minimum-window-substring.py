class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if(len(t)>len(s)):
            return ""
        
        ans = ""
        dic = {}
        for e in t:
            dic[e] = dic.get(e, 0)+1
        
        l = 0
        for r in range(len(s)):
            ch = s[r]
            if(ch in dic):
                dic[ch]-=1
            
            while(max(dic.values())==0):
                sub = s[l:r+1]
                if(not ans or len(sub)<len(ans)):
                    ans = sub
                
                c = s[l]
                if(c in dic):
                    dic[c]+=1
                l+=1
                
        return ans