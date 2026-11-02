# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: TreeNode | None, startValue: int, destValue: int) -> str:
        
        graph = {}
        def dfs(root):
            if(not root):
                return 
            if(root.val not in graph):
                graph[root.val] = set()

            if(root.left):
                if(root.left.val not in graph):
                    graph[root.left.val] = set()
                graph[root.val].add(('L', root.left.val))
                graph[root.left.val].add(('U', root.val))
                dfs(root.left)

            if(root.right):
                if(root.right.val not in graph):
                    graph[root.right.val] = set()
                graph[root.val].add(('R', root.right.val))
                graph[root.right.val].add(('U', root.val))
                dfs(root.right)

            return

        dfs(root)

        visited = set()
        q = [(startValue, "")]
        visited.add(startValue)

        while(q):
            q_ = []
            while(q):
                nde, s = q.pop()
                if(nde == destValue):
                    return s
                neigh = graph.get(nde, set())

                for e, n in neigh:
                    if(n not in visited):
                        q_.append((n, s+e))
                        visited.add(n)
            q = q_
        return ""