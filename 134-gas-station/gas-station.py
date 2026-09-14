class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        sm = 0
        ans = 0
        fuel = 0
        for i in range(len(gas)):
            delta = (gas[i]-cost[i])
            sm += delta
            fuel += delta
            if(fuel<0):
                ans = i+1
                fuel = 0
        if(sm<0):
            return -1
        return ans