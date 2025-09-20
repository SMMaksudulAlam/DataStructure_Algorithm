class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pr = {}
        for c, p in prerequisites:
            if(c not in pr):
                pr[c] = []
            pr[c].append(p)

        completed = {}
        def dfs(c, dic):
            if(c not in pr):
                return True
            if(c in dic):
                return False
            dic[c] = 1
            for p in pr[c]:
                complete = dfs(p, dic)
                if(not complete):
                    return False
            del pr[c]
            return True
        
        for c in range(numCourses):
            if(c in pr):
                complete = dfs(c, {})
                if(not complete):
                    return False
        return True
