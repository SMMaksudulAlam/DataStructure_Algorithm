class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        completed = set()
        has_loop = set()

        in_path = set()

        def traverse(nde):
            if(nde in in_path):
                return False
            if(nde in completed):
                return True

            in_path.add(nde)
            neigh = graph[nde]

            can_complete = True
            for n in neigh:
                can_complete = can_complete and traverse(n)

            if(not can_complete):
                has_loop.add(nde)
            else:
                completed.add(nde)
            in_path.remove(nde)

            return can_complete

        for nde in range(len(graph)):
            traverse(nde)
        
        completed = list(completed)
        completed.sort()
        return completed