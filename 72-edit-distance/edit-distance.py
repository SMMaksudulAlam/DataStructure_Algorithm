class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = {}
        def count_dis(ind1, ind2):
            if((ind1, ind2) in dp):
                return dp[(ind1, ind2)]
            if(ind1<0 or ind2<0):
                if(ind1<0):
                    return ind2+1
                else:
                    return ind1+1
            ans = 0
            if(word1[ind1] == word2[ind2]):
                ans += count_dis(ind1-1, ind2-1)
            else:
                ans1 = 1 + count_dis(ind1-1, ind2-1) #replace
                ans2 = 1 + count_dis(ind1-1, ind2) #delete
                ans3 = 1 + count_dis(ind1, ind2-1) #insert
                ans += min(ans1, ans2, ans3)
            
            dp[(ind1, ind2)] = ans
            return ans
        
        ans = count_dis(len(word1)-1, len(word2)-1)
        return ans