class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        """
        dp = {}
        def count_DS(indS, indT):
            if((indS, indT) in dp):
                return dp[(indS, indT)]
            if(indT<0):
                return 1
            if(indS<0):
                return 0
            ans = 0
            if(s[indS] == t[indT]):
                ans += count_DS(indS-1, indT-1)
            ans += count_DS(indS-1, indT)
            dp[(indS, indT)] = ans
            return ans

        ans = count_DS(len(s)-1, len(t)-1)
        return ans
        """

        s1 = t
        s2 = s
        dp = [[0]*(len(s2)+1) for _ in range(len(s1)+1)]
        for i in range(len(s2)+1):
            dp[0][i] = 1
        for ind1 in range(1, len(s1)+1):
            for ind2 in range(1, len(s2)+1):
                ind1_ = ind1-1
                ind2_ = ind2-1
                if(s1[ind1_] == s2[ind2_]):
                    dp[ind1][ind2] += dp[ind1-1][ind2-1]
                dp[ind1][ind2] += dp[ind1][ind2-1]
        return dp[-1][-1]