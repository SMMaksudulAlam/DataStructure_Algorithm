import heapq as hq
class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph = {}
        for u, v, d in edges:
            if(u not in graph):
                graph[u] = []
            if(v not in graph):
                graph[v] = []
            graph[u].append((v, d))
            graph[v].append((u, d))
        
        ans = {}

        for i in range(n):
            st = set()
            h = []
            hq.heappush(h, (0, i))

            while(h):
                dis, u = hq.heappop(h)
                if(u in st):
                    continue
                
                st.add(u)
                lst = graph.get(u, [])

                for v, d in lst:
                    final_dis = d+dis
                    if(final_dis>distanceThreshold):
                        continue
                    if(v not in st):
                        hq.heappush(h, (final_dis, v))
            
            ans[i] = st
            
        ans_node = 0
        ans_negh = len(ans.get(0, set()))

        for k, v in ans.items():
            if(len(v)<ans_negh):
                ans_node = k
                ans_negh = len(v)
            elif(len(v) == ans_negh):
                if(k>ans_node):
                    ans_node = k
            else:
                pass
        return ans_node


