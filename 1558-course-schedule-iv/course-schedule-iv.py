class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = {}
        for p, c in prerequisites:
            if(c not in graph):
                graph[c] = set()
            graph[c].add(p)
        
        completed = set()
        track = set()
        preq = {}

        def dfs(c):
            if(c in completed):
                return True, preq[c]
            if(c not in graph):
                pr = set()
                pr.add(c)
                completed.add(c)
                preq[c] = pr
                return True, pr
            
            if(c in track):
                return False, set()
            
            track.add(c)
            prs = set()
            prs.add(c)
            for p in graph[c]:
                com, prs_ = dfs(p)
                if(not com):
                    return False, set()
                for pr in prs_:
                    prs.add(pr)
            
            completed.add(c)
            preq[c] = prs

            return True, prs

        for i in range(numCourses):
            if(i not in completed):
                dfs(i)
        
        #print(preq)
        ans = []
        for p, c in queries:
            if(c not in preq):
                ans.append(False)
            else:
                if(p not in preq[c]):
                    ans.append(False)
                else:
                    ans.append(True)
        return ans

            