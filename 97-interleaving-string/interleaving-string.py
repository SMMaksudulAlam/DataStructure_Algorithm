class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if(len(s1)+len(s2)!=len(s3)):
            return False

        if(len(s1)>len(s2)):
            s1, s2 = s2, s1
        s1 = 'X'+s1
        s2 = 'X'+s2
        s3 = 'X'+s3
        
        ans = [[False]*(len(s2)) for _ in range(len(s1))]

        for i in range(len(s2)):
            if(s3[i]==s2[i]):
                ans[0][i] = True
            else:
                break
        
        for i in range(len(s1)):
            if(s3[i]==s1[i]):
                ans[i][0] = True
            else:
                break

        for i in range(1, len(s1)):
            for j in range(1, len(s2)):
                ans[i][j] = (s3[i+j]==s2[j] and ans[i][j-1]) or (s3[i+j]==s1[i] and ans[i-1][j])
        
        #print(s1, s2, ans)
        
        return ans[-1][-1]