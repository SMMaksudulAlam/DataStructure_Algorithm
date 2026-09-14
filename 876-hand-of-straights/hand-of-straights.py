class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if(len(hand)%groupSize != 0):
            return False
        
        expected_group_count = len(hand)//groupSize

        freq = {}
        for e in hand:
            freq[e] = freq.get(e, 0)+1
        
        q = []
        for k, v in freq.items():
            q.append([k, v])
        
        q.sort(key = lambda x:x[0])
        q = deque(q)

        left = 0
        count = 0
        while(q):
            if(len(q)<groupSize):
                return False
            mini = math.inf
            for i in range(groupSize):
                if(i>0):
                    if(q[i][0]!=q[i-1][0]+1):
                        return False
                mini = min(mini, q[i][1])
            count += mini
            if(mini == 0):
                return False
            for i in range(groupSize):
                q[i][1] -= mini
            while(q and q[0][1]==0):
                q.popleft()
        if(count == expected_group_count):
            return True
        return False