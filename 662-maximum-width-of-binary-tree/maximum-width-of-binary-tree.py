# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        q = deque()
        ans = 0
        q.append((root, 0))

        while(q):
            ans = max(ans, q[-1][1]-q[0][1]+1)
            q_ = deque()

            while(q):
                nde, ind = q.popleft()
                if(nde.left):
                    q_.append((nde.left, ind*2))
                if(nde.right):
                    q_.append((nde.right, ind*2+1))
            if(q_):
                q = q_
        
        return ans
        
