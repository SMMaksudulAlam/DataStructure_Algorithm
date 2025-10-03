import heapq as hq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {}
        for u, v, t in times:
            if(u not in graph):
                graph[u] = []
            graph[u].append((t, v))

        h = []
        track = set()
        time = set()
        
        hq.heappush(h, (0, k))

        while(h):
            t, v = hq.heappop(h)
            if(v in track):
                continue
            track.add(v)
            time.add(t)

            if(v in graph):
                lst = graph[v]
                for t_, v_ in lst:
                    if(v_ not in track):
                        hq.heappush(h, (t+t_, v_))
        
        if(len(track)!=n):
            return -1
        return max(time)

