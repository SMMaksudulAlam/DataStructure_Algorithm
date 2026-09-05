class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        """
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
        """

        """
        visited = set()
        ans = 0
        ln = len(isConnected)
        def traverse_province(i):
            visited.add(i)
            for j in range(ln):
                if(isConnected[i][j]==1 and j not in visited):
                    traverse_province(j)
            return

        for k in range(ln):
            if(k not in visited):
                ans+=1
                traverse_province(k)
        return ans
        """

        #DFS
        length = len(isConnected)
        visited = set()
        def traverse(i):
            if(i in visited):
                return
            
            visited.add(i)
            for j in range(length):
                if(isConnected[i][j] == 1):
                    traverse(j)
            return 
        
        count = 0
        for i in range(length):
            if(i not in visited):
                count+=1
                traverse(i)
        return count

                