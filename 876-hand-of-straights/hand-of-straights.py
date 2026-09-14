class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if(len(hand)%groupSize != 0):
            return False
        
        expected_group_count = len(hand)//groupSize

        freq = {}
        for e in hand:
            freq[e] = freq.get(e, 0)+1

        left = 0
        count = 0
        while(freq):
            keys = list(freq.keys())
            for k in keys:
                if(k+1 not in freq):
                    mini = math.inf
                    for i in range(groupSize):
                        ky = k - i
                        if(ky not in freq):
                            return False
                        mini = min(mini, freq[ky])

                    count += mini
                    for i in range(groupSize):
                        ky = k - i
                        freq[ky] -= mini
                        if(freq[ky]==0):
                            del freq[ky]
                    break

        if(count == expected_group_count):
            return True
        return False