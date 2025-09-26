class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s = "X"+s
        p = "X"+p

        ans = []
        row = [False]*len(s)
        row[0] = True
        ans.append(row)

        for i in range(1, len(p)):
            row = [False]*len(s)
            if(p[i]=='*'):
                row[0] = ans[-2][0]
            ans.append(row)

        for i in range(1, len(p)):
            for j in range(1, len(s)):
                if(p[i]==s[j]):
                    ans[i][j] = ans[i-1][j-1]
                if(p[i]=='.'):
                    ans[i][j] = ans[i-1][j-1]
                elif(p[i]=='*'):
                    #print(i, j, p[i], s[j])
                    ans[i][j] = ans[i-2][j]
                    if(p[i-1] =='.' or p[i-1] == s[j]):
                        ans[i][j] = ans[i][j] or ans[i][j-1]
                else:
                    pass
        return ans[-1][-1]
