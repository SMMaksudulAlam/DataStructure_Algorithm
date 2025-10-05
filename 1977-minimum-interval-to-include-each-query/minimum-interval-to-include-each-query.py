import heapq as hq
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        ind_map = {}
        for i, e in enumerate(queries):
            ind_map[i] = e

        intervals.sort(key = lambda x:x[0])        
        queries.sort()
        h = []
        i = 0
        q = 0
        ans_dic = {}
        while(q<len(queries)):

            qry = queries[q]
            while(i<len(intervals) and intervals[i][0]<=qry):
                hq.heappush(h, (intervals[i][1]-intervals[i][0]+1, intervals[i][0]))
                i+=1

            while(h and h[0][1]+h[0][0]-1<qry):
                hq.heappop(h)

            if(not h):
                ans_dic[qry] = -1
            else:
                ans_dic[qry] = h[0][0]
            q+=1
        
        ans=[]
        for k, v in ind_map.items():
            ans.append(ans_dic[v])
        return ans