class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = {}

        def color_nodes(nde, clr):
            if(nde in color):
                if(color[nde] != clr):
                    return False
                return True
            
            color[nde] = clr

            clr = 1-clr
            neigh = graph[nde]
            for n in neigh:
                if(not color_nodes(n, clr)):
                    return False
            return True
        
        for n in range(len(graph)):
            if(n not in color):
                ans = color_nodes(n, 0)
                if(not ans):
                    return False

        return True
