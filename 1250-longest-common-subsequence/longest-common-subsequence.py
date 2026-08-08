class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        #The trick "Only consider character that contribute to the length of LCS" at building time does not do its job. For example, a='aabbb', b='baa'. The returned length is correct (2), but the printed string is 'ba' — and 'ba' is not a subsequence of a='aabbb'. So the best option is to do fill the dp table first, then backtrack.


        lcs_str = "" #To print the lcs
        track_len = 1
        dp = {}
        def LCS(ind1, ind2):
            nonlocal lcs_str
            nonlocal track_len
            if((ind1, ind2) in dp):
                return dp[(ind1, ind2)]
            if(ind1<0 or ind2<0):
                return 0
            ans = 0
            if(text1[ind1] == text2[ind2]):
                ans = 1 + LCS(ind1-1, ind2-1)
            else:
                ans = max(LCS(ind1, ind2-1), LCS(ind1-1, ind2))
            
            dp[(ind1, ind2)] = ans

            if(ans==track_len): #Only consider character that contribute to the length of LCS
                lcs_str += text1[ind1]
                track_len += 1
            return ans

        ans = LCS(len(text1)-1, len(text2)-1)
        print(lcs_str)
        return ans
        
        """
        if(len(text1)>len(text2)):
            text1, text2 = text2, text1

        ln1 = len(text1)
        ln2 = len(text2)

        prev = [0]*(ln2+1)

        lcs_str = "" #To print the lcs
        track_len = 1
        for ind1 in range(ln1):
            cur = [0]*(ln2+1)
            for j in range(1, ln2+1):
                ind2 = j-1
                if(text1[ind1] == text2[ind2]):
                    cur[j] = prev[j-1] + 1
                    if(cur[j]==track_len): #Only consider character that contribute to the length of LCS
                        lcs_str += text1[ind1]
                        track_len += 1
                else:
                    cur[j] = max(prev[j], cur[j-1])
            prev = cur

        print(lcs_str)
        return prev[-1]
        """