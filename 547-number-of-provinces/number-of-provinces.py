class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        graph = {}
        ln = len(isConnected)
        for i in range(ln):
            for j in range(ln):
                if(i!=j and isConnected[i][j] == 1):
                    if(i not in graph):
                        graph[i] = []
                    if(j not in graph):
                        graph[j] = []
                    graph[i].append(j)
        #print(graph)
        ans = 0
        def traverse_province(i):
            visited.add(i)
            neigh = graph.get(i, [])
            for n in neigh:
                if(n not in visited):
                    traverse_province(n)
            return

        for k in range(ln):
            if(k not in visited):
                ans+=1
                traverse_province(k)
        return ans

                
                