# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        # definition of boundary in the question is very very very important. assuming the left/right most node on left/right boundary is not aligned to the definition
        left = []
        def traverse_left(root, on_left_boundary):
            if(not root):
                return
            if(root.left == None and root.right == None):
                left.append(root.val)
                return
            
            if(on_left_boundary):
                left.append(root.val)
                if(root.left):
                    traverse_left(root.left, True)
                    traverse_left(root.right, False)
                else:
                    traverse_left(root.right, True)
            else:
                traverse_left(root.left, False)
                traverse_left(root.right, False)
            return
        
        right = []

        def traverse_right(root, on_right_boundary):
            if(not root):
                return
            if(root.left == None and root.right == None):
                right.append(root.val)
                return
            
            if(on_right_boundary):
                right.append(root.val)
                if(root.right):
                    traverse_right(root.right, True)
                    traverse_right(root.left, False)
                else:
                    traverse_right(root.left, True)
            else:
                traverse_right(root.right, False)
                traverse_right(root.left, False)
            return
        
        traverse_left(root.left, True)
        traverse_right(root.right, True)
        #print(left, right)
        return [root.val] + left + right[::-1]
            

            

