class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dic = {}
        for e in t:
            dic[e] = dic.get(e, 0) + 1
        
        left = 0
        found = False
        ans = s
        for right in range(len(s)):
            ch = s[right]
            if(ch in dic):
                dic[ch] -= 1
            
            while(max(dic.values())<=0):
                length = right - left + 1
                found = True
                if(len(ans)>length):
                    ans = s[left:right+1]
                ch = s[left]
                if(ch in dic):
                    dic[ch] += 1
                left+=1

        if(found):
            return ans
        else:
            return ""

