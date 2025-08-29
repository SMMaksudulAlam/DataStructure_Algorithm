# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        def findGoods(root, mx):
            nonlocal count
            if(not root):
                return
            if(root.val>=mx):
                count+=1
            mx = max(mx, root.val)
            findGoods(root.left, mx)
            findGoods(root.right, mx)
            return
        
        findGoods(root, root.val)
        return count