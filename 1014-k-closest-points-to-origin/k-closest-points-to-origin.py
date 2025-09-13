import heapq as hq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []
        for p in points:
            h.append((p[0]*p[0]+p[1]*p[1], p))

        hq.heapify(h)
        res = []
        for i in range(k):
            res.append(hq.heappop(h)[1])

        return res

        