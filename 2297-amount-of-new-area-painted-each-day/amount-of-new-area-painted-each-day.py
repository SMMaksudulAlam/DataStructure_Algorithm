class node:
    def __init__(self, l_end, r_end):
        self.left= l_end
        self.right = r_end
        self.left_child = None
        self.right_child = None

class Solution:
    def amountPainted(self, paint: list[list[int]]) -> list[int]:
        """
        def traverse(root, l, r):
            if(l >= root.left and r <= root.right):
                return 0
            
            if(l < root.left and r > root.right):
                left_ans = 0
                right_ans = 0

                if(root.left_child == None):
                    root.left_child = node(l, root.left)
                    left_ans = root.left - l
                else:
                    left_ans = traverse(root.left_child, l, root.left)
                
                if(root.right_child == None):
                    root.right_child = node(root.right, r)
                    right_ans = r - root.right
                else:
                    right_ans = traverse(root.right_child, root.right, r)

                return left_ans + right_ans 

            elif(l < root.left):
                ans = 0
                if(root.left_child == None):
                    root.left_child = node(l, min(root.left, r))
                    ans = min(root.left, r) - l
                else:
                    ans = traverse(root.left_child, l, min(root.left, r))
                return ans
            
            elif(r > root.right):
                ans = 0
                if(root.right_child == None):
                    root.right_child = node(max(root.right, l), r)
                    ans = r - max(root.right, l)
                else:
                    ans = traverse(root.right_child, max(root.right, l), r)
                return ans
            else:
                pass
            return -1
        
        ans = []
        root = None
        for s, e in paint:
            if(root == None):
                root = node(s, e)
                seg = e-s
                ans.append(seg)
            else:
                seg = traverse(root, s, e)
                ans.append(seg)
        return ans

        # TC --> (nlogn) x, it actually can be (n^2) for the case 1-5, 5-7, 8-10 ....
        #gets TLE
        """

        """
        track = [0]*(5**4)
        ans = []
        for s, e in paint:
            count = 0
            while(s<=e):
                if(track[s] == 0):
                    count += 1
                    track[s] = 1
                s+=1
            ans.append(count)
        return ans
        #this scanning algo does not work here. suppose for interval [4, 5], but 1-4, 5-7 is already done. it will return 0, but answer should be 1
        """

        chain = {}
        ans = []
        for s, e in paint:
            count = 0
            while(s<e):
                if(s in chain):
                    x = chain[s]
                    chain[s] = max(x, e)
                    s = x
                else:
                    count+=1
                    chain[s] = e
                    s+=1
            ans.append(count)
        return ans



