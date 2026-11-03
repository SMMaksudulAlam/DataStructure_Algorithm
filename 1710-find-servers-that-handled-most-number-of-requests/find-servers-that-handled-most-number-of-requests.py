from sortedcontainers import SortedList 
import heapq as hq
class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        available = SortedList()
        for i in range(k):
            available.add(i)
        h = []
        dic = {}
        
        for i in range(len(arrival)):
            arrival_time = arrival[i]
            end_time = arrival[i] + load[i]

            pos = i%k

            while(h and h[0][0]<=arrival_time):
                e_time, pos_ = hq.heappop(h)
                available.add(pos_)

            if(available):
                ind = available.bisect_left(pos) % len(available)
                avail_pos = available[ind]
                dic[avail_pos] = dic.get(avail_pos, 0) + 1

                available.remove(avail_pos)
                hq.heappush(h, (end_time, avail_pos))
        
        ans = []
        maxi = max(dic.values())
        for k, v in dic.items():
            if(v==maxi):
                ans.append(k)
        return ans