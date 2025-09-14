class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if(n==1):
            return True
        graph = {}
        for x, y in edges:
            if(x not in graph):
                graph[x] = set()
            if(y not in graph):
                graph[y] = set()
            graph[x].add(y)
            graph[y].add(x)

        visited = {}

        def dfs(node):
            if(node in visited):
                return False
            visited[node] = 1
            if(node not in graph):
                return False
            for neigh in graph[node]:
                graph[neigh].remove(node)
                res = dfs(neigh)
                if(not res):
                    return False
            return True
        
        res = dfs(0)
        if(not res):
            return False
        
        for i in range(n):
            if(i not in visited):
                return False
        return True
