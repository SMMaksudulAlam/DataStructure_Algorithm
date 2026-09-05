import heapq as hq
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        graph = {i: set() for i in range(n)}
        for (s, d, t) in roads:
            graph[s].add((d, t))
            graph[d].add((s, t))

        time = {0:0}
        ways = {0:1}
        mod = 10**9 + 7
        h = []
        hq.heappush(h, (0, 0))

        while(h):
            (cost, nde) = hq.heappop(h)
            if(nde in time and time[nde]<cost):
                continue
            neigh = graph[nde]
            for (d, t) in neigh:
                if(cost + t < time.get(d, math.inf)):
                    hq.heappush(h, (cost+t, d))
                    time[d] = cost+t
                    ways[d] = ways[nde]
                elif(cost + t == time.get(d, math.inf)):
                    ways[d] = (ways[d] + ways[nde])%mod
                else:
                    pass
        #print(time, ways)
        return ways.get(n-1, 0)
            
            
