class Solution:
    def minmaxGasDist(self, stations: List[int], k: int) -> float:
        def cover_station(dis):
            nonlocal k
            used_k = 0
            for i in range(1, len(stations)):
                gap = stations[i] - stations[i-1]
                used_k += (ceil(gap/dis) - 1)
                if(used_k>k):
                    return False
            return True


        stations.sort()

        left = 0
        right = stations[-1]
        
        while(left<=right):
            #print(left, right)
            if(right-left<=0.000001):
                return left
            
            mid = (left+right)/2.0
            #print('for mid:', mid, cover_station(mid), left, right)
            if(cover_station(mid)):
                right = mid
            else:
                left = mid
        return -1

                