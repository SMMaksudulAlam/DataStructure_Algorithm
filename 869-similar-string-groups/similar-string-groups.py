class Solution:
    def numSimilarGroups(self, strs: list[str]) -> int:
        length = len(strs[0])

        def check_simi(s1, s2):
            count = 0
            for i in range(length):
                if(s1[i]!=s2[i]):
                    count +=1
            if(count <= 2):
                return True
            return False
        
        graph = {i: set() for i in range(len(strs))}

        for i in range(len(strs)):
            for j in range(i+1, len(strs)):
                s1 = strs[i]
                s2 = strs[j]
                if(check_simi(s1, s2)):
                    graph[i].add(j)
                    graph[j].add(i)
        #graph = {0: {1}, 1: {0, 2}, 2: {1}, 3: {}}

        visited = set() # {0, 1, 2}
        def dfs(nde, p): #0, -1 | 1, 0
            if(nde in visited):
                return
            
            visited.add(nde) 
            neigh = graph[nde] #{1} | {0, 2}

            for nei in neigh:
                if(nei != p):
                    dfs(nei, nde)
            return
        
        ans = 0
        for i in range(len(strs)):
            if(i not in visited):
                dfs(i, -1)
                ans += 1
        return ans

        #TC --> O(n*n*length)            