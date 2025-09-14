class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        dic = {}
        for c, p in prerequisites:
            if(c not in dic):
                dic[c] = []
            dic[c].append(p)
        
        ans = []
        completed = set()
        track = {}
        def dfs(c):
            if(c in track):
                return False
            if(c not in dic):
                if(c not in completed):
                    ans.append(c)
                    completed.add(c)
                return True
            track[c] = 1

            for p in dic[c]:
                comp = dfs(p)
                if(not comp):
                    return False
            ans.append(c)
            completed.add(c)
            del track[c]
            del dic[c]
            return True
        
        for i in range(numCourses):
            comp = dfs(i)
            if(not comp):
                return []
        return ans
            