# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: TreeNode | None, startValue: int, destValue: int) -> str:
        """
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
        """

        #it works. the following one is just another approach by determining the start_path and end_path individually

        def dfs(root, val):
            if(not root):
                return False, ""
            
            if(root.val == val):
                return True, ""
            
            left, s = dfs(root.left, val)
            if(left):
                return True, s+'L' #will reverse letter
            
            right, s = dfs(root.right, val)
            if(right):
                return True, s+'R' #will reverse letter
            
            return False, ""
        
        start, start_path = dfs(root, startValue)
        start_path = start_path[::-1]
        
        dest, dest_path = dfs(root, destValue)
        dest_path = dest_path[::-1]

        i = 0
        mini_length = min(len(start_path), len(dest_path))

        while(i<mini_length and start_path[i] == dest_path[i]):
            i+=1
        
        ans = "U"*(len(start_path)-i) + dest_path[i:]
        return ans

