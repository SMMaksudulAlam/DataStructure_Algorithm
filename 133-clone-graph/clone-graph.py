"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        dic = {}
        track = {}
        def dfs(node):
            if(node.val in track):
                return dic[node.val]
            track[node.val] = 1
            if(node.val not in dic):
                new_node = Node(node.val)
                dic[node.val] = new_node
            new_node = dic[node.val]
            for neigh in node.neighbors:
                neigh_new = dfs(neigh)
                new_node.neighbors.append(neigh_new)
            return new_node
        
        if(not node):
            return None
        new_node = dfs(node)
        return new_node
