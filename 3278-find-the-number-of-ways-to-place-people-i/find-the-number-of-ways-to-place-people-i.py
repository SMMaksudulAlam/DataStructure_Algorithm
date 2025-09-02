import heapq as hq
class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        h = []
        ln = len(points)
        for x, y in points:
            hq.heappush(h, (x, -y))
        
        points = []
        while(h):
            x, y = hq.heappop(h)
            y = -y
            points.append([x, y])

        #print(points)
        
        count = 0
        for i in range(ln-1):
            y1 = points[i][1]
            for j in range(i+1, ln):
                y2 = points[j][1]
                if(y1>=y2):
                    isThere = False
                    for k in range(i+1, j):
                        y3 = points[k][1]
                        if(y2<=y3<=y1):
                            isThere = True
                            break
                    if(not isThere):
                        count+=1
        return count