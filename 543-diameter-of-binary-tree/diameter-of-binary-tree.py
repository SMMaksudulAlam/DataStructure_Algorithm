# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def diam(root):
            nonlocal ans
            if(not root):
                return 0
            
            left = diam(root.left)
            right = diam(root.right)

            temp_ans = left + right + 1
            ans = max(ans, left+right)

            return max(left, right) + 1
        
        diam(root)
        return ans