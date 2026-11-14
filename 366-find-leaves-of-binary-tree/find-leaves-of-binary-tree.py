# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import heapq as hq
class Solution:
    def findLeaves(self, root: TreeNode | None) -> list[list[int]]:
        h = []

        def dfs(root):
            if(root.left == None and root.right == None):
                hq.heappush(h, (0, root.val))
                return 0
            
            left_level = 0
            right_level = 0

            if(root.left):
                left_level = dfs(root.left)
            if(root.right):
                right_level = dfs(root.right)
            
            level = 1 + max(left_level, right_level)
            hq.heappush(h, (level, root.val))

            return level
        
        dfs(root)
        ans = []
        lvl = 0
        while(h):
            temp = []
            while(h and h[0][0]==lvl):
                temp.append(h[0][1])
                hq.heappop(h)
            ans.append(temp)
            lvl += 1
        return ans