class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        pre = strs[0]

        for i in range(1, len(strs)):
            s = strs[i]
            j = 0
            while(j<min(len(pre), len(s))):
                if(s[j]!=pre[j]):
                    break
                j+=1
            pre = pre[:j]
            
            if(not pre):
                return ""

        return pre