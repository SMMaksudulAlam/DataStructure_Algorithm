# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(root, left_val, right_val):
            if(not root):
                return True
            
            if(not left_val < root.val < right_val):
                return False

            return validate(root.left, left_val, root.val) and validate(root.right, root.val, right_val)

        return validate(root, -math.inf, math.inf)