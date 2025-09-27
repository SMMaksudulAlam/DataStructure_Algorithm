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
            y_max_limit = y+1

            for j in range(i+1, len(points)):
                x_, y_ = points[j]
                if(y_>=y_max_limit):
                    continue
                if(y_min_limit < y_ < y_max_limit):
                    count += 1
                if(y_<=y):
                    y_min_limit = max(y_min_limit, y_)

        return count


