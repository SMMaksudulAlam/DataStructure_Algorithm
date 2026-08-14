class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {}
        for c, p in prerequisites:
            if(c not in graph):
                graph[c] = []
            graph[c].append(p)

        completed = set()
        has_loop = set()
        ans = []
        in_path = set()

        def traverse(nde):
            if(nde in in_path):
                return False
            if(nde in completed):
                return True

            in_path.add(nde)
            neigh = graph.get(nde, [])

            for n in neigh:
                if(not traverse(n)):
                    return False

            completed.add(nde)
            ans.append(nde)
            in_path.remove(nde)
            return True

        for nde in range(numCourses):
            if(not traverse(nde)):
                return []
        return ans