class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dic = {}
        ans = [0]*(len(s)+1)
        for w in wordDict:
            if(len(w)<=len(s)):
                dic[w] = len(w)
                if(s[:len(w)] in dic):
                    ans[len(w)] = 1
        
        if(ans[-1]==1):
            return True
        
        for i in range(len(s)):
            if(ans[i]==1):
                for k, v in dic.items():
                    if(i+v<=len(s) and s[i:i+v] in dic):
                        ans[i+v] = 1
        
        if(ans[-1]==1):
            return True
        
        return False