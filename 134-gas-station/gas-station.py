class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        i = 0
        while(i<len(gas)):
            travel = True
            tank = gas[i]
            tank-=cost[i]
            for j in range(len(gas)):
                ind = (i+1+j)%len(gas)
                if(tank<0):
                    travel = False
                    if(ind>i):
                        i = ind
                        break
                    else:
                        return -1
                tank+=gas[ind]
                tank-=cost[ind]
            if(travel):
                return i
        return -1