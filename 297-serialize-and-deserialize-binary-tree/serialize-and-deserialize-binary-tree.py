# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """

        ans = []
        def traverse(root):
            if(not root):
                ans.append('n')
                return
            ans.append(str(root.val))
            traverse(root.left)
            traverse(root.right)

        traverse(root)
        #print(ans)
        return ",".join(ans)
       



    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        lst = data.split(',')
        q = deque(lst)

        def build():
            if(not q):
                return None
            ch = q.popleft()
            if(ch == 'n'):
                return None
            
            val = int(ch)
            nde = TreeNode()
            nde.val = val

            left = build()
            right = build()

            nde.left = left
            nde.right = right
            return nde

        return build()
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))