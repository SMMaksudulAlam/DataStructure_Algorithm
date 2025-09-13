import heapq as hq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        dic = {}
        for t in tasks:
            dic[t] = dic.get(t, 0)+1
        
        h = []
        for k, v in dic.items():
            h.append((-v))

        hq.heapify(h)
        
        q = deque()


        intv = 0
        while(q or h):
            if(h):
                t = hq.heappop(h)
                t+=1
                if(t<0):
                    q.append((intv+n, t))
            
            if(q):
                if(q[0][0]==intv):
                    tm, t = q.popleft()
                    hq.heappush(h, t)
            
            intv+=1

        return intv