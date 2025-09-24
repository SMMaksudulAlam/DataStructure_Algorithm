class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dic = {0:1}

        for i in range(len(nums)):
            e = nums[i]
            dic_ = {}
            for k in dic.keys():
                k_ = k+e
                dic_[k_] = dic_.get(k_, 0) + dic[k]
                k_ = k-e
                dic_[k_] = dic_.get(k_, 0)  + dic[k]
            dic = dic_

        ans = 0
        if(target in dic):
            ans = dic[target]
        return ans