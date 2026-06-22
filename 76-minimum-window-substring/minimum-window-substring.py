class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ans = ""
        dic = {}
        for ch in t:
            dic[ch] = dic.get(ch, 0) + 1
        
        left = 0
        for right in range(len(s)):
            if(s[right] in dic):
                dic[s[right]] -= 1
                
            while(max(dic.values())==0):
                if(not ans or right-left+1 < len(ans)):
                    ans = s[left:right+1]
                if(s[left] in dic):
                    dic[s[left]] += 1
                left+=1  

        return ans