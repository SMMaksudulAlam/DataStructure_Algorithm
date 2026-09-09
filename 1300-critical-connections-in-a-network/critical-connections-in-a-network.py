class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph = {i: set() for i in range(n)}
        for (u, v) in connections:
            graph[u].add(v)
            graph[v].add(u)
        
        visited = set()
        rank = {}
        order = 1
        ans = []
        def traverse(nde, parent):
            #print(parent, nde, rank)
            nonlocal order
            if(nde in visited):
                #print("visited the node:", nde)
                return rank[nde]
            visited.add(nde)
            rank[nde] = order
            order+=1
            neigh = graph[nde]

            ret_val = rank[nde]
            for n in neigh:
                if(n == parent):
                    continue
                child_val = traverse(n, nde)
                if(child_val > rank[nde]):
                    #print("inserting: ", (nde, n))
                    ans.append([nde, n])
                ret_val = min(ret_val, child_val)    
            #print("returning", nde, rank, ret_val)
            rank[nde] = ret_val             
            return ret_val
        
        traverse(0, -1)
        return ans