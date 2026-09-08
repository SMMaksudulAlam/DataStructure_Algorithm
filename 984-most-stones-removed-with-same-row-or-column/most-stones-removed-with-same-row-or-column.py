class uf:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.count = 1
        self.parent = self
    def find(self):
        cur = self
        while(cur != cur.parent):
            cur = cur.parent
        
        nde = self
        while(nde != cur):
            temp = nde.parent
            nde.parent = cur
            nde = temp
        return cur

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        rows = {}
        cols = {}
        nodes = {}
        parents = set()

        for (r, c) in stones:
            nde = uf(r, c)
            nodes[(r, c)] = nde
            parents.add((r, c))

            if(r not in rows):
                rows[r] = []
            if(c not in cols):
                cols[c] = []
            rows[r].append((r, c))
            cols[c].append((r, c))


        for (r, row) in rows.items():
            nde1 = nodes[row[0]]
            for ind in range(1, len(row)):
                nde2 = nodes[row[ind]]

                pr1 = nde1.find()
                pr2 = nde2.find()
                
                if(pr1 != pr2):
                    pr1.count += pr2.count
                    pr2.parent = pr1
                    parents.remove((pr2.x, pr2.y))

        for (c, col) in cols.items():
            nde1 = nodes[col[0]]
            for ind in range(1, len(col)):
                nde2 = nodes[col[ind]]

                pr1 = nde1.find()
                pr2 = nde2.find()
                
                if(pr1 != pr2):
                    pr1.count += pr2.count
                    pr2.parent = pr1
                    parents.remove((pr2.x, pr2.y))
        
        ans = 0
        for p in parents:
            ans += (nodes[p].count-1)
        return ans