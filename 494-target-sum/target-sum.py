class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}
        def count_ways(rem, ind):
            if((rem, ind) in dp):
                return dp[(rem, ind)]
            if(ind < 0):
                if(rem == 0):
                    return 1
                return 0
            
            num = nums[ind]
            pos = count_ways(rem - num, ind-1)
            neg = count_ways(rem + num, ind-1)

            dp[(rem, ind)] = pos + neg
            return dp[(rem, ind)]

        return count_ways(target, len(nums)-1)