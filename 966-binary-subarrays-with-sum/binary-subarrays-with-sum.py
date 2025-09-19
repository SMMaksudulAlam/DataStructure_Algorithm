class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        s = 0
        ans = 0
        dic = {0:1}
        for e in nums:
            s+=e
            rem = s - goal
            if(rem in dic):
                ans += dic[rem]
            dic[s] = dic.get(s, 0)+1
        return ans