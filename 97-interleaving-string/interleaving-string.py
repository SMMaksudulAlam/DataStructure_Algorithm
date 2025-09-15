class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if(len(s1)+len(s2)!=len(s3)):
            return False

        if(len(s1)>len(s2)):
            s1, s2 = s2, s1
        
        ans = [[False]*(len(s2)+1) for _ in range(len(s1)+1)]

        ans[0][0] = True

        for i in range(1, len(s2)+1):
            if(s3[i-1]==s2[i-1]):
                ans[0][i] = True
            else:
                break
        
        for i in range(1, len(s1)+1):
            if(s3[i-1]==s1[i-1]):
                ans[i][0] = True
            else:
                break

        for i in range(1, len(s1)+1):
            for j in range(1, len(s2)+1):
                ans[i][j] = (s3[i+j-1]==s2[j-1] and ans[i][j-1]) or (s3[i+j-1]==s1[i-1] and ans[i-1][j])
        
        #print(s1, s2, ans)
        
        return ans[-1][-1]