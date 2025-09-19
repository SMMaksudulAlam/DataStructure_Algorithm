class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        s = 0
        ans = 0
        dic = {}
        for e in nums:
            s+=e
            if(s==goal):
                ans+=1
            rem = s - goal
            if(rem in dic):
                ans += dic[rem]
            dic[s] = dic.get(s, 0)+1
        return ans