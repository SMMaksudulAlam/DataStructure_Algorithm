class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        flights = {}
        for (src, des) in tickets:
            if(src not in flights):
                flights[src] = []
            flights[src].append(des)
        
        for val in flights.values():
            val.sort(reverse = True)

        #print(flights)
        ans = []
        def dfs(src):
            if(src not in flights):
                ans.append(src)
                return
            while(flights[src]):
                src_ = flights[src].pop()
                dfs(src_)
            ans.append(src)
            return
        
        dfs("JFK")

        return ans[::-1]