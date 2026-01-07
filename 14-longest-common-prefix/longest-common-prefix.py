class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = strs[0]
        if(not ans):
            return ""
        
        for i in range(1, len(strs)):
            s = strs[i]
            if(len(s)<len(ans)):
                ans, s = s, ans
            ln = len(ans)
            for j in range(ln):
                if(ans[j]!=s[j]):
                    ans = ans[:j]
                    break
            if(not ans):
                return ""
        return ans