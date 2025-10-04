class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        dic = {}
        for d, a in tickets:
            if(d not in dic):
                dic[d] = []
            dic[d].append(a)

        for k in dic.keys():
            dic[k].sort()
            dic[k] = deque(dic[k])

        ans = []

        def dfs(d):
            if(d in dic):
                while(dic[d]):
                    dfs(dic[d].popleft())
            ans.append(d)
        
        dfs("JFK")

        return ans[::-1]