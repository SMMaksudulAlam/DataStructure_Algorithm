class node:
    def __init__(self, val):
        self.val = val
        self.parent = self
        self.count = 1
    def find(self):
        while(self.parent != self):
            self = self.parent
        return self

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if(len(edges)!=n-1):
            return False   
        dic = {}
        parent = set()
        for i in range(n):
            dic[i] = node(i)
            parent.add(i)

        for u, v in edges:
            u_parent = dic[u].find()
            v_parent = dic[v].find()

            if(u_parent != v_parent):
                if(u_parent.count>=v_parent.count):
                    v_parent.parent = u_parent
                    u_parent.count += v_parent.count
                    parent.remove(v_parent.val)
                else:
                    u_parent.parent = v_parent
                    v_parent.count += u_parent.count
                    parent.remove(u_parent.val)

        if(len(parent)>1):
            return False
        
        prnt = None
        for p in parent:
            prnt = p

        print(dic[prnt].count)
        if(dic[prnt].count!=n):
            return False

        return True