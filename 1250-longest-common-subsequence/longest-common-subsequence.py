class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        dp = {}
        def LCS(ind1, ind2):
            if((ind1, ind2) in dp):
                return dp[(ind1, ind2)]
            if(ind1<0 or ind2<0):
                return 0
            ans = 0
            if(text1[ind1] == text2[ind2]):
                ans = 1 + LCS(ind1-1, ind2-1)
            else:
                ans = max(LCS(ind1-1, ind2-1), LCS(ind1, ind2-1), LCS(ind1-1, ind2))
            
            dp[(ind1, ind2)] = ans
            return ans

        ans = LCS(len(text1)-1, len(text2)-1)
        return ans
        """
        
        if(len(text1)>len(text2)):
            text1, text2 = text2, text1

        ln1 = len(text1)
        ln2 = len(text2)

        prev = [0]*(ln2+1)

        for ind1 in range(ln1):
            cur = [0]*(ln2+1)
            for j in range(1, ln2+1):
                ind2 = j-1
                if(text1[ind1] == text2[ind2]):
                    cur[j] = prev[j-1] + 1
                else:
                    cur[j] = max(prev[j-1], prev[j], cur[j-1])
            prev = cur

        return prev[-1]