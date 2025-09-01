import heapq as hq
class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        h = []
        for p, t in classes:
            curr = p/t
            delta = (p+1)/(t+1) - curr
            hq.heappush(h, (-delta, (p, t)))
        
        for i in range(extraStudents):
            delta, (p, t) = hq.heappop(h)
            p+=1
            t+=1
            curr = p/t
            delta = (p+1)/(t+1) - curr
            hq.heappush(h, (-delta, (p, t)))
        
        ratio_sum = 0
        
        while(h):
            delta, (p, t) = hq.heappop(h)
            ratio_sum += (p/t)

        return ratio_sum/len(classes)
