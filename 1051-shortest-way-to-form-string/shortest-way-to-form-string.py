class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        dic = {}
        for i, e in enumerate(source):
            if(e not in dic):
                dic[e] = []
            dic[e].append(i)
        
        ans = 0
        cur_pos = -1

        for e in target:
            if(e not in dic):
                return -1
            lst = dic[e]
            ind = bisect.bisect_left(lst, cur_pos+1)
            if(ind==len(lst)):
                ans+=1
                cur_pos = lst[0]
            else:
                cur_pos = lst[ind]

        ans += 1
        return ans