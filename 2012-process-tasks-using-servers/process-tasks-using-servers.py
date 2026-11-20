import heapq as hq
class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        available = [] #(weight, id)
        occupied = [] #(end_time, id)
        ans = []

        for i, e in enumerate(servers):
            hq.heappush(available, (e, i))

        time = 0
        for ind in range(len(tasks)):
            
            if(not available):
                time = occupied[0][0]
            else:
                time = max(time, ind) #it is ciritical.

            while(occupied and occupied[0][0]<=time):
                _, id = hq.heappop(occupied)
                hq.heappush(available, (servers[id], id))

            end_time = time+tasks[ind]
            _, id = hq.heappop(available)
            hq.heappush(occupied, (end_time, id))
            ans.append(id)

        return ans
        #TC --> klogn