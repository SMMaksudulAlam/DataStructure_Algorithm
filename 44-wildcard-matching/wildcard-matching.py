class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s = 'X'+s
        p = 'X'+p
        l2 = len(s)
        l1 = len(p)

        ans = []
        for i in range(l1):
            row = [False]*l2
            ans.append(row)
        ans[0][0] = True
        for i in range(1, l1):
            if(p[i]=='*'):
                ans[i][0] = ans[i-1][0]

        for i in range(1, l1):
            for j in range(1, l2):
                if(p[i]==s[j]):
                    ans[i][j] = ans[i-1][j-1]
                elif(p[i]=='?'):
                    ans[i][j] = ans[i-1][j-1]
                elif(p[i]=='*'):
                    ans[i][j] = ans[i][j-1] or ans[i-1][j]
                else:
                    ans[i][j] = False
        return ans[-1][-1]