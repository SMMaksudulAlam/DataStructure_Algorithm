import heapq as hq
class Solution:
    def maximumScore(self, scores: list[int], edges: list[list[int]]) -> int:
        """
        graph = {}
        for u, v in edges:
            if(u not in graph):
                graph[u] = set()
            if(v not in graph):
                graph[v] = set()
            
            graph[u].add(v)
            graph[v].add(u)
        
        path = set()
        ans = -1
        def dfs(nde, p, score_sum, depth):
            nonlocal ans

            if(nde in path):
                return 

            path.add(nde)

            if(depth == 4):
                ans = max(ans, score_sum)
                path.remove(nde)  #i forgot this line --> thus the path got dirty
                return 

            neigh = graph[nde]
            for n in neigh:
                if(n==p):
                    continue
                dfs(n, nde, score_sum+scores[n], depth+1)
            
            path.remove(nde)
            return
        
        for k in graph.keys():
            path = set()
            dfs(k, -1, scores[k], 1)
        return ans

        #TC --> O(n^4)
        """

        #now let's see the problem from a different angle. i need to know a-b-c-d, right? if b-c is known, which is all the edges given, we can simply idenitfy a and d and get the answer.
        
        graph = {}
        for u, v in edges:
            if(u not in graph):
                graph[u] = []
            if(v not in graph):
                graph[v] = []
            
            graph[u].append((scores[v], v))
            graph[v].append((scores[u], u))
        
        for v in graph.values():
            v.sort(key = lambda x:x[0], reverse = True)

        ans = -1
        for u, v in edges:
            scr = scores[u]+scores[v]
            neigh_u = graph[u]
            neigh_v = graph[v]

            _u = None
            i = 0
            while(i<len(neigh_u)):
                if(neigh_u[i][1]!= v):
                    _u = neigh_u[i][1]
                    break
                i+=1
            v_ = None
            i = 0
            while(i<len(neigh_v)):
                if(neigh_v[i][1] != u and neigh_v[i][1] != _u):
                    v_ = neigh_v[i][1]
                    break
                i+=1
            if(_u != None and v_ != None):
                ans = max(ans, scr+scores[_u]+scores[v_])
            

            v_ = None
            i = 0
            while(i<len(neigh_v)):
                if(neigh_v[i][1] != u):
                    v_ = neigh_v[i][1]
                    break
                i+=1
            _u = None
            i = 0
            while(i<len(neigh_u)):
                if(neigh_u[i][1] != v and neigh_u[i][1] != v_):
                    _u = neigh_u[i][1]
                    break
                i+=1
            if(_u != None and v_ != None):
                ans = max(ans, scr+scores[_u]+scores[v_])

        return ans