class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        left = 0
        right = 0
        for i in range(2, len(cost)+1):
            temp = right
            right = min(left+cost[i-2], right+cost[i-1])
            left = temp
        return right
