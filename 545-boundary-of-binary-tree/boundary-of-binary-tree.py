# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        """
        # this is the code on assumption of left/right most nodes of each level are on left/right boundary.
        left_level = set()
        left = []

        def traverse_left(root, level):
            if(not root):
                return
            if(root.left == None and root.right == None):
                left_level.add(level)
                left.append(root.val)
                return
            
            if(level not in left_level):
                left_level.add(level)
                left.append(root.val)

            traverse_left(root.left, level+1)
            traverse_left(root.right, level+1)

            return
        
        right_level = set()
        right = []

        def traverse_right(root, level):
            if(not root):
                return
            if(root.left == None and root.right == None):
                right_level.add(level)
                right.append(root.val)
                return
            
            if(level not in right_level):
                right_level.add(level)
                right.append(root.val)

            traverse_right(root.right, level+1)
            traverse_right(root.left, level+1)

            return
        
        traverse_left(root.left, 1)
        traverse_right(root.right, 1)
        return [root.val] + left + right[::-1]
        """

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
            

            

