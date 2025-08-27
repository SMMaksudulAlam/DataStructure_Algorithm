import heapq as hq
class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        h = []
        v = []

        for x1, y1, x2, y2 in rectangles:
            hq.heappush(h, (y1, y2))
            hq.heappush(v, (x1, x2))

        
        #checking horizontals
        #print(h, v)
        py1, py2 = hq.heappop(h)
        while(h and h[0][0]<py2):
            py2 = max(py2, h[0][1])
            hq.heappop(h)
        
        while(h):
            y1, y2 = hq.heappop(h)
            while(h and h[0][0]<y2):
                y2 = max(y2, h[0][1])
                hq.heappop(h)
            if(h):
                return True
            py2 = max(py2, y2)

        px1, px2 = hq.heappop(v)
        while(v and v[0][0]<px2):
            px2 = max(px2, v[0][1])
            hq.heappop(v)

        while(v):
            x1, x2 = hq.heappop(v)
            while(v and v[0][0]<x2):
                x2 = max(x2, v[0][1])
                hq.heappop(v)
            if(v):
                return True
            px2 = max(px2, x2)

        return False
