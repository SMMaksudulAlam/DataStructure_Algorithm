import heapq as hq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = {}
        for ch in tasks:
            freq[ch] = freq.get(ch, 0)+1

        h = []
        for k, v in freq.items():
            hq.heappush(h, (-v, 0, k))
        
        q = deque()
        time = 0
        while(h or q):
            while(q and q[0][1]<=time):
                hq.heappush(h, q.popleft())
            
            while(h and h[0][1]>time):
                q.append(hq.heappop(h))
            
            if(h):
                (count, t, task) = hq.heappop(h)
                count = -count
                count-=1
                if(count>0):
                    hq.heappush(h, (-count, time + n + 1, task))
            
            time +=1
        return time