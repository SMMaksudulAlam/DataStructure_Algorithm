class node:
    def __init__(self, val):
        self.val = val
        self.parent = self
        self.count = 1
    def find(self):
        while(self != self.parent):
            self = self.parent
        return self

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dic = {}
        parent = set()
        for i in range(n):
            nde = node(i)
            dic[i] = nde
            parent.add(i)

        for x, y in edges:
            xN = dic[x]
            yN = dic[y]

            xN_p = xN.find()
            yN_p = yN.find()

            if(xN_p!=yN_p):
                if(xN_p.count>=yN_p.count):
                    yN_p.parent = xN_p
                    xN_p.count+=yN_p.count
                    parent.remove(yN_p.val)
                else:
                    xN_p.parent = yN_p
                    yN_p.count+=xN_p.count
                    parent.remove(xN_p.val)

       
        return len(parent)
