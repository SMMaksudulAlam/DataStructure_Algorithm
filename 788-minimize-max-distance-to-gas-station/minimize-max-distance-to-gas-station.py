import heapq as hq
class Solution:
    def minmaxGasDist(self, stations: List[int], k: int) -> float:
        """
        dist = []
        for i in range(1, len(stations)):
            dis = stations[i]-stations[i-1]
            hq.heappush(dist, (-dis, (dis, 1)))
        
        for i in range(k):
            split, (dis, count) = hq.heappop(dist)
            split = dis/((count+1)*1.0)
            hq.heappush(dist, (-split, (dis, count+1)))

        split, (dis, count) = dist[0]
        return -split
        """


        """
        def count_new_stations(max_dis):
            count = 0
            last_pos = stations[0]
            i = 1
            while(last_pos<stations[-1]):
                if(last_pos + max_dis < stations[i]):
                    count+=1
                    last_pos += max_dis
                else:
                    last_pos = stations[i]
                    i+=1
            return count
        """

        gaps = [stations[i]-stations[i-1] for i in range(1, len(stations))]
        
        def count_new_stations(max_dis):
            count = 0
            for gap in gaps:
                count += (math.ceil(gap/max_dis) - 1)
            return count

        left = 0
        right = 0
        for i in range(1, len(stations)):
            right = max(right, stations[i]-stations[i-1])
        
        ans = 0
        threshold = 10**(-6)
        while(right-left>threshold):
            mid = (left+right)/2.0
            count = count_new_stations(mid)
            if(count<=k):
                ans = mid
                right = mid
            else:
                left = mid
        return ans