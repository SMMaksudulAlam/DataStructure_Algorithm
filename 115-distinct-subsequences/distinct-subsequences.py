class Solution:
    def numDistinct(self, s: str, t: str) -> int:
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
            