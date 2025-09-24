class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dic = {0:1}

        for i in range(len(nums)):
            e = nums[i]
            dic_ = {}
            for k in dic.keys():
                k_ = k+e
                dic_[k_] = dic_.get(k_, 0) + dic.get(k, 0)
                k_ = k-e
                dic_[k_] = dic_.get(k_, 0)  + dic.get(k, 0)
            dic = dic_

        ans = 0
        if(target in dic):
            ans = dic[target]
        return ans

        