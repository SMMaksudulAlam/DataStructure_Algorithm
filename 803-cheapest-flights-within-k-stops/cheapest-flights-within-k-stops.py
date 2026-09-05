import heapq as hq
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = {}
        for (frm, to, price) in flights:
            if(frm not in graph):
                graph[frm] = set()
            graph[frm].add((to, price))

        h = []
        hq.heappush(h, (0, -1, src))
        visited = {}

        while(h):
            (price, stp, src) = hq.heappop(h)
            if(src == dst and stp <= k):
                return price
            
            if(((src, stp) in visited and visited[(src, stp)]<=price) or stp>=k):
                continue

            visited[(src, stp)]=price
            neigh = graph.get(src, [])

            for (ngh, p) in neigh:
                if(((ngh, stp+1) not in visited) and stp+1<=k):
                    hq.heappush(h, (price+p, stp+1, ngh))
        
        return -1