import heapq as hq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = []
        for e in stones:
            hq.heappush(h, -e)
        
        while(len(h)>1):
            s1 = -hq.heappop(h)
            s2 = -hq.heappop(h)

            diff = abs(s1-s2)
            if(diff>0):
                hq.heappush(h, -diff)
        
        if(h):
            return -h[0]
        return 0
        
