import heapq as hq
class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        graph = {i: set() for i in range(n)}
        for u, v, w in edges:
            graph[u].add((v, w))
        
        visited = set() #node, last_char, count
        h = []
        h.append((0, 0, labels[0], 1)) #weight_sum, node, last_char, count

        while(h):
            w_s, nde, ch, count = hq.heappop(h)
            if(nde == n-1):
                return w_s
            
            if((nde, ch, count) in visited):
                continue

            visited.add((nde, ch, count)) #i missed this line in the prior submission
            
            neigh = graph[nde]
            for next_nde, w in neigh:
                next_w_s = w_s + w
                next_ch = labels[next_nde]
                next_count = 1 if(ch != next_ch) else count + 1
                if(next_count <= k):
                    hq.heappush(h, (next_w_s, next_nde, next_ch, next_count))
        
        return -1

        #TC --> O(e*log(v))
            

            