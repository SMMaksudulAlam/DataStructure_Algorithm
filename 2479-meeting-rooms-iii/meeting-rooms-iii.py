import heapq as hq
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        m = []
        for (s, e) in meetings:
            hq.heappush(m, (s, e))

        dic = {}
        h = []
        for i in range(n):
            dic[i] = 0
            hq.heappush(h, (0, i))
        #print(m, h, dic)

        while(m):
            (ms, me) = hq.heappop(m)
            diff = me-ms

            lst = []
            while(h and h[0][0]<=ms):
                (ce, cr) = hq.heappop(h)
                lst.append((ms, cr))
            
            while(lst):
                hq.heappush(h, lst.pop())

            (re, rr) = hq.heappop(h)

            dic[rr]+=1
            if(re<=ms):
                hq.heappush(h, (me, rr))
            else:
                hq.heappush(h, (re+diff, rr))

            #print(ms, me, re, rr, m, h)

        #print(m, h, dic)
        ans = []
        for (k, v) in dic.items():
            hq.heappush(ans, (-v, k))

        return ans[0][1]
        
        
        

