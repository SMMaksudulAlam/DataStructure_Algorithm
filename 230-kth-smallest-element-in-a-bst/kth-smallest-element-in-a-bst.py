# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        def traverse(root):
            nonlocal k
            if(not root):
                return None
            
            if(root.left == None and root.right == None):
                k-=1
                if(k == 0):
                    return root.val
                return None
            
            val = traverse(root.left)
            if(val != None):
                return val

            k-=1
            if(k==0):
                return root.val

            val = traverse(root.right)

            return val
        
        val = traverse(root)
        return val