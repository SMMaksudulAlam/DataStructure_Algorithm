class Solution:
    def collectTheCoins(self, coins: List[int], edges: List[List[int]]) -> int:
        dic = {}
        for (x, y) in edges:
            if(x not in dic):
                dic[x] = set()
            if(y not in dic):
                dic[y] = set()
            dic[x].add(y)
            dic[y].add(x)
        
        """
        keys = list(dic.keys())
        q = deque()
        dic_ = {}
        track = set()
        for k in keys:
            if(len(dic[k])==1 and coins[k]==0):
                del dic[k]
                continue
            if(coins[k]==0):
                dic_[k] = [0, 0, 0]
            else:
                dic_[k] = [1, 0, 0]
                if(len(dic[k])==1):
                    q.append(k)
                    track.add(k)
        print(dic_)
        while(q):
            q_ = deque()
            track2 = set()
            while(q):
                n = q.popleft()
                track.add(n)
                for nxt in dic[n]:
                    if(nxt not in dic):
                        continue
                    if(nxt not in track):
                        dic_[nxt][1]+=dic_[n][0]
                        dic_[nxt][2]+=dic_[n][1]
                    if(nxt not in track2 and nxt not in track):
                        q_.append(nxt)
                        track2.add(nxt)
            q = q_
            for n in track2:
                track.add(n)
            print(n, dic_, q, track)
        
        print(dic_)
        """
        #print(dic)
        q = deque()
        for k in dic.keys():
            if(len(dic[k])==1 and coins[k]==0):
                q.append(k)
        
        while(q):
            n = q.pop()
            p = None
            for x in dic[n]:
                p = x
                dic[p].remove(n)
                if(len(dic[p])==1 and coins[p]==0):
                    q.append(p)
            del dic[n]
            #print(f"deleting {n}")
            
        q = deque()
        for k in dic.keys():
            if(len(dic[k])==1 and coins[k]==1):
                q.append(k)

        #print(f"now, {q}, {dic}")
        itr = 0
        while(itr<2):
            q_ = deque()
            while(q):  
                n = q.pop()
                p = None
                for x in dic[n]:
                    p = x
                    dic[p].remove(n)
                    if(len(dic[p])==1):
                        q_.append(p)
                del dic[n]
                #print(f"deleting {n}")
            q = q_
            #print(f"now again, q: {q}")
            itr+=1
        #print(dic)
        return max(0, (len(dic.keys())-1)*2)




        


