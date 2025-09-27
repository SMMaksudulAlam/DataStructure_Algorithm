import heapq as hq
class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x:x[0])
        h = []
        for x, y in points:
            h.append((x, -y))
        
        hq.heapify(h)
        points = []
        while(h):
            x, y = hq.heappop(h)
            points.append((x, -y))

        count = 0
        for i in range(len(points)):
            x, y = points[i]

            y_min_limit = -inf

            for j in range(i+1, len(points)):
                x_, y_ = points[j]
                if(y_>y):
                    continue
                if(y_min_limit < y_ <= y):
                    count += 1
                    y_min_limit = y_

        return count


