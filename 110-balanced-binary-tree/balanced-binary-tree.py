# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if(not root):
            return True
        
        def is_balanced(root):
            if(not root):
                return True, 0
            is_true_left, left = is_balanced(root.left)
            is_true_right, right = is_balanced(root.right)
            max_depth =  1 + max(left, right)
            if((not is_true_left) or (not is_true_right) or abs(left-right) > 1):
                return False, max_depth
            return True, max_depth

        is_true, depth = is_balanced(root)
        return is_true