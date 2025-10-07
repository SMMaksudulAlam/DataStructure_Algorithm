import heapq as hq
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        graph = {}
        for u, v, t in roads:
            if(u not in graph):
                graph[u] = []
            if(v not in graph):
                graph[v] = []
            
            graph[u].append((v, t))
            graph[v].append((u, t))
        
        dic = {0: (0, 1)}
        h = []
        hq.heappush(h, (0, 0))
        mod = 10**9+7

        while(h):
            time, u = hq.heappop(h)
            if(time != dic[u][0]):
                continue
            path_count = dic[u][1]

            lst = graph.get(u, [])
            for v, t in lst:
                tme = t+time
                if(v not in dic):
                    dic[v] = (tme, path_count)
                    hq.heappush(h, (tme, v))
                else:
                    if(dic[v][0]<tme):
                        pass
                    elif(dic[v][0]==tme):
                       dic[v] = (tme, (path_count+dic[v][1])%mod)
                    else:
                        dic[v] = (tme, path_count)
                        hq.heappush(h, (tme, v))
            
        ans = dic.get(n-1, [])
        return ans[-1] if ans else -1
        