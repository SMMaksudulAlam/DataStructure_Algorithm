class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        points.sort()
        count = 1

        print(points)

        limit = points[0][1]

        for i in range(1, len(points)):
            if(points[i][0]<=limit):
                limit = min(limit, points[i][1])
            else:
                count += 1
                limit = points[i][1]
        
        return count