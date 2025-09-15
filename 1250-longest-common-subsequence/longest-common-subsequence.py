class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if(len(text1)>len(text2)):
            text1, text2 = text2, text1
        
        text1 = 'X'+text1
        text2 = 'X'+text2

        ans = [[1]*len(text2) for _ in range(len(text1))]

        for i in range(1, len(text1)):
            for j in range(1, len(text2)):
                if(text1[i]==text2[j]):
                    ans[i][j] = ans[i-1][j-1]+1
                else:
                    ans[i][j] = max(ans[i-1][j-1], ans[i-1][j], ans[i][j-1])
        return ans[-1][-1]-1