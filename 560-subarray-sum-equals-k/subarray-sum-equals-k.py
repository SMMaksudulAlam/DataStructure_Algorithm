class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dic = {0:1}
        sm = 0
        ans = 0

        for n in nums:
            sm+=n
            res = sm-k
            if(res in dic):
                ans+=dic[res]
            dic[sm] = dic.get(sm, 0) + 1
            
        return ans