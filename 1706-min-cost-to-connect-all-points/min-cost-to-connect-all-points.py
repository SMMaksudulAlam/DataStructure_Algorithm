import heapq as hq

class uf:
    def __init__(self, id):
        self.count = 1
        self.parent = self
        self.id = id
        self.dis = 0
    
    def find(self):
        while(self!=self.parent):
            self = self.parent
        return self



class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        dis = []
        parents = set()
        dic = {}

        for i in range(len(points)):
            nde = uf(i)
            dic[i] = nde
            parents.add(i)
        
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                x1, y1 = points[i]
                x2, y2 = points[j]
                d = abs(x1-x2) + abs(y1-y2)
                dis.append((d, i, j))
        
        hq.heapify(dis)

        while(dis):
            d, p1, p2 = hq.heappop(dis)
            parent_p1 = dic[p1].find()
            parent_p2 = dic[p2].find()
            
            if(parent_p1 != parent_p2):
                if(parent_p1.count>=parent_p2.count):
                    parent_p2.parent = parent_p1
                    parent_p1.count += parent_p2.count
                    parent_p1.dis += (parent_p2.dis + d)
                    parents.remove(parent_p2.id)
                else:
                    parent_p1.parent = parent_p2
                    parent_p2.count += parent_p1.count
                    parent_p2.dis += (parent_p1.dis + d)
                    parents.remove(parent_p1.id)
            if(parent_p1.count == len(points) or parent_p1.count == len(points)):
                if(parent_p1.count == len(points)):
                    return parent_p1.dis
                else:
                    return parent_p2.dis
        return 0


       