class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        def subsets(ind):
            if(ind < 0):
                return [[]], [[]]
            total, local = subsets(ind-1)
            total_, local_ = total[:], []
            if(ind==0 or nums[ind]!=nums[ind-1]):
                for e in total:
                    e = e + [nums[ind]]
                    total_.append(e)
                    local_.append(e)
            else:
                for e in local:
                    e = e + [nums[ind]]
                    total_.append(e)
                    local_.append(e)
            return total_, local_

        ans, ans_ = subsets(len(nums)-1)
        return ans
