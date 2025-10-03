class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {}
        for c, p in prerequisites:
            if(c not in graph):
                graph[c] = []
            graph[c].append(p)
        
        dic = {}
        completed = set()
        ans = []

        def dfs(c):
            if(c in completed):
                return True
            
            if(c not in graph):
                completed.add(c)
                ans.append(c)
                return True

            if(c in dic):
                return False

            dic[c] = 1
            for p in graph[c]:
                comp = dfs(p)
                if(not comp):
                    return False
                    
            completed.add(c)
            ans.append(c)
            return True
        
        for i in range(numCourses):
            comp = dfs(i)
            if(not comp):
                return []
        return ans
