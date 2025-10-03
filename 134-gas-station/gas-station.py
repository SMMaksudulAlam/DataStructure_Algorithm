class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        i = 0
        while(i<len(gas)):
            tank = gas[i]
            tank-=cost[i]
            if(tank<0):
                i+=1
                continue
            traveled = True
            for j in range(len(gas)):
                ind = (i+1+j)%len(gas)
                tank += (gas[ind]-cost[ind])
                if(tank>=0):
                    pass
                else:
                    traveled = False
                    if(ind+1>i):
                        i = ind+1
                    else:
                        return -1
                    break
            if(traveled):
                return i
        return -1