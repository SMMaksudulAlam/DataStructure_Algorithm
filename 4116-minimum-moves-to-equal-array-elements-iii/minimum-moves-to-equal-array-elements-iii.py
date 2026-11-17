class Solution:
    def minMoves(self, nums: List[int]) -> int:
        maxi = -1
        sm = 0
        for e in nums:
            maxi = max(maxi, e)
            sm += e
        return maxi*len(nums) - sm