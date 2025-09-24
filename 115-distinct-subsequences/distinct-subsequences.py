class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        text1, text2 = t, s
        
        text1 = 'X'+text1
        text2 = 'X'+text2

        ans = [[1]*len(text2)]
        for _ in range(len(text1)-1):
            row = [0]*len(text2)
            ans.append(row)

        for i in range(1, len(text1)):
            for j in range(1, len(text2)):
                if(text1[i]==text2[j]):
                    ans[i][j] = ans[i-1][j-1]+ans[i][j-1]
                else:
                    ans[i][j] = ans[i][j-1]
        return ans[-1][-1]