# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        preorder = deque(preorder)
        dic = {}
        for i, e in enumerate(inorder):
            dic[e] = i

        def build(s, e):
            if(s>e):
                return None
            nde = TreeNode()
            val = preorder.popleft()
            ind = dic[val]

            left = build(s, ind-1)
            right = build(ind+1, e)

            nde.val = val
            nde.left = left
            nde.right = right

            return nde
        
        root = build(0, len(inorder)-1)
        return root


