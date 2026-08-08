class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
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