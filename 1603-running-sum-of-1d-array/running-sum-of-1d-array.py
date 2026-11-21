class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        prefix = 0
        ans = []
        for e in nums:
            prefix += e
            ans.append(prefix)
        return ans