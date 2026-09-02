# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        def flatten_(root):
            if(not root):
                return root, root
            
            left = root.left
            right = root.right

            root.left = None
            root.right = None
            head = root
            tail = root

            if(left):
                left_head, left_tail = flatten_(left)
                tail.right = left_head
                tail = left_tail
            
            if(right):
                right_head, right_tail = flatten_(right)
                tail.right = right_head
                tail = right_tail
            
            return head, tail
        
        head, tail = flatten_(root)
        return head
            