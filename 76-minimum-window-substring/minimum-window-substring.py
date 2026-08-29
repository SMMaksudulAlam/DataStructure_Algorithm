class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dic = {}
        for e in t:
            dic[e] = dic.get(e, 0) + 1
        
        left = 0
        found = False
        ans = s
        counter_zero_feq = 0
        for right in range(len(s)):
            ch = s[right]
            if(ch in dic):
                dic[ch] -= 1
                if(dic[ch] == 0):
                    counter_zero_feq += 1
            
            while(counter_zero_feq == len(dic.keys())):
                length = right - left + 1
                found = True
                if(len(ans)>length):
                    ans = s[left:right+1]
                ch = s[left]
                if(ch in dic):
                    dic[ch] += 1
                    if(dic[ch] == 1):
                        counter_zero_feq -= 1
                left+=1

        if(found):
            return ans
        else:
            return ""

