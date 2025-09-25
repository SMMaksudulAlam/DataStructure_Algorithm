class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        dic = {}
        def burst(s, e):
            if(s>e):
                return 0
            
            key = (s, e)
            if(key in dic):
                return dic[key]

            res = -inf
            for i in range(s, e+1):
                left = nums[s-1] if(s>0) else 1
                mid = nums[i]
                right = nums[e+1] if(e<len(nums)-1) else 1

                r = left*mid*right + burst(s, i-1) + burst(i+1, e)
                res = max(res, r)

            dic[key] = res
            return res
        
        ans = burst(0, len(nums)-1)
        return ans