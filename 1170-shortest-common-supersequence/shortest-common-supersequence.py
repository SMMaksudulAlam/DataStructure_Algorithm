class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        """
        #it works but gets MLE
        dp = {}
        def build(ind1, ind2):
            if((ind1, ind2) in dp):
                return dp[(ind1, ind2)]
            if(ind1<0 or ind2<0):
                if(ind1<0):
                    return str2[:ind2+1]
                return str1[:ind1+1]
            ans = None
            if(str1[ind1] == str2[ind2]):
                ans = build(ind1-1, ind2-1) + str1[ind1]
            else:
                ans1 = build(ind1-1, ind2) + str1[ind1]
                ans2 = build(ind1, ind2-1) + str2[ind2]

                if(len(ans1)<len(ans2)):
                    ans = ans1
                else:
                    ans = ans2
            dp[(ind1, ind2)] = ans
            return dp[(ind1, ind2)]
        
        ans = build(len(str1)-1, len(str2)-1)
        return ans
        """

        s1 = str1
        s2 = str2
        if(len(s1)>len(s2)):
            s1, s2 = s2, s1
        dp = [[0]*(len(s2)+1) for _ in range(len(s1)+1)]
		
        for ind1 in range(1, len(s1)+1):
            for ind2 in range(1, len(s2)+1):
                ind1_ = ind1-1
                ind2_ = ind2-1
                if(s1[ind1_] == s2[ind2_]):
                    dp[ind1][ind2] = dp[ind1-1][ind2-1] + 1
                else:
                    dp[ind1][ind2] = max(dp[ind1-1][ind2], dp[ind1][ind2-1])
		
		
        s = ""
        ind1 = len(dp)-1
        ind2 = len(dp[0])-1
        #print(dp)

        while(True):
            if(ind1 == 0 or ind2 ==0):
                if(ind1==0):
                    s = s2[:ind2] + s
                else:
                    s = s1[:ind1] + s
                break
            if(s1[ind1-1] == s2[ind2-1]):
                s = s1[ind1-1] + s
                ind1-=1
                ind2-=1
            elif(dp[ind1][ind2] == dp[ind1-1][ind2]):
                s = s1[ind1-1] + s
                ind1-=1
            elif(dp[ind1][ind2] == dp[ind1][ind2-1]):
                s = s2[ind2-1] + s
                ind2-=1
            else:
                pass
        return s