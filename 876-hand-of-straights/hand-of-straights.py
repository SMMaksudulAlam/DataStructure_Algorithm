import heapq as hq
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if(len(hand)%groupSize != 0):
            return False
        dic = {}
        for e in hand:
            dic[e] = dic.get(e, 0)+1
        
        count = 0
        while(dic):
            lst = list(dic.keys())
            for k in lst:
                if(k+1 not in dic):
                    c = 0
                    while(k in dic):
                        c+=1
                        dic[k]-=1
                        if(dic[k]==0):
                            del dic[k]
                        if(c == groupSize):
                            count += 1
                            break
                        k-=1
            #print(count, dic)
        return count == len(hand)//groupSize

            
