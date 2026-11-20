class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        logs.sort(key = lambda e: e[1]) #[[1,3], [1,5], [2,6]]

        q = queries[:]
        
        queries.sort()

        track = {}
        p_ind = 0
        l_ind = 0
        count = 0

        ans_map = {}
        for e in queries:
            if(e in ans_map):
                continue
            s = e-x
            while(p_ind < len(logs) and logs[p_ind][1]<=e):
                s_id, time = logs[p_ind]
                if(s_id not in track or track[s_id] == 0):
                    count += 1
                    track[s_id] = 1
                else:
                    track[s_id] += 1
                p_ind+=1
            
            while(l_ind < len(logs) and logs[l_ind][1]<s):
                s_id, time = logs[l_ind]
                if(track[s_id] == 1):
                    count -= 1
                    track[s_id] = 0
                else:
                    track[s_id] -= 1
                l_ind += 1
            
            ans_map[e] = n - count
        
        ans = []
        for e in q:
            ans.append(ans_map[e])
        
        return ans

        #TC --> O(nlogn)