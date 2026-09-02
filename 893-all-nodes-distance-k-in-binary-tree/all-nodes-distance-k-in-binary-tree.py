# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = {}
        def build_graph(root):
            if(not root):
                return
            if(root.val not in graph):
                graph[root.val] = set()
            
            if(root.left):
                if(root.left.val not in graph):
                    graph[root.left.val] = set()
                graph[root.val].add(root.left.val)
                graph[root.left.val].add(root.val)
            
            if(root.right):
                if(root.right.val not in graph):
                    graph[root.right.val] = set()
                graph[root.val].add(root.right.val)
                graph[root.right.val].add(root.val)

            build_graph(root.left)
            build_graph(root.right)
            return
        build_graph(root)
        #print(graph)

        ans = []
        def dfs(nde, p, dist):
            if(dist == 0):
                ans.append(nde)
                return
            
            neigh = graph.get(nde, [])
            for ngh in neigh:
                if(ngh == p):
                    continue
                dfs(ngh, nde, dist-1)
            return
        
        dfs(target.val, -1, k)
        return ans
