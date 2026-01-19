class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        for n in nums:
            ans_ = []
            for a in ans:
                ans_.append(a)
                ans_.append(a+[n])
            ans = ans_
        return ans
