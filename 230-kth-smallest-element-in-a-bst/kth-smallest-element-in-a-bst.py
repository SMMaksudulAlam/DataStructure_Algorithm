# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        ans = None
        def traverse(root):
            nonlocal ans
            nonlocal count
            if(not root):
                return
            traverse(root.left)
            count +=1
            if(count == k):
                ans = root.val
            traverse(root.right)
            return

        traverse(root)
        return ans