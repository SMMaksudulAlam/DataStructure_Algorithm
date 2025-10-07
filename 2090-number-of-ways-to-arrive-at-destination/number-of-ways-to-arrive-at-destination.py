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
        
        count = 0
        dic = {0:(0, 1)}
        local = []
        hq.heappush(local, (0, 0))
        mod = 10**9 + 7
        #print(graph)
        while(local):
            #print(local)
            t, u = hq.heappop(local)
            lst = graph.get(u, [])
            time, path_count = dic[u]
            #print("~~~~~~~", t, u, time, path_count, lst)
            if(time != t):
                continue
            for v, t_dist in lst:
                t_ = time + t_dist
                if(v not in dic):
                    #print(">>>>", v, t_, path_count, u, dic)
                    dic[v] = (t_, path_count)
                    hq.heappush(local, (t_, v))
                    #print("after:", v, t_, path_count, u, dic)
                else:
                    if(t_>dic[v][0]):
                        pass
                    elif(t_==dic[v][0]):
                        dic[v] = (t_, (dic[v][1]+path_count) % mod)
                    else:
                        #print(v, t_, path_count, u, dic)
                        dic[v] = (t_, path_count)
                        hq.heappush(local, (t_, v))

        #print(dic)
        ans = dic.get(n-1, [])
        return ans[-1] if ans else -1



        
