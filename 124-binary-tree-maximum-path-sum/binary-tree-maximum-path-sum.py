# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = -inf
        def max_path_sum(root):
            nonlocal ans
            if(not root):
                return -inf
            
            left = max_path_sum(root.left)
            right = max_path_sum(root.right)

            l2r = left + right + root.val
            l_ = left + root.val
            r_ = right + root.val

            ans = max(ans, l2r, l_, r_, left, right, root.val)

            return root.val + max(left, right, 0)

        max_path_sum(root)
        return ans