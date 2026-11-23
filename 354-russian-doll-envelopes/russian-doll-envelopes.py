class Solution:
    def maxEnvelopes(self, envelopes: list[list[int]]) -> int:
        """
        envelopes.sort(key = lambda x: x[0])
        track = {i: 1 for i in range(len(envelopes))}
        
        next_length = deque()
        next_height = deque()

        length_q = deque()
        height_q = deque()

        len_envelope = len(envelopes)
        for i in range(len_envelope-1, -1, -1):
            l, h = envelopes[i]
            while(length_q and length_q[0][0]<=l):
                length_q.popleft()
            while(height_q and height_q[0][0]<=h):
                height_q.popleft()
            
            if(not length_q):
                next_length.appendleft(len_envelope)
                length_q.appendleft((l, i))
            else:
                next_length.appendleft(length_q[0][1])
                length_q.appendleft((l, i))
            
            if(not height_q):
                next_height.appendleft(len_envelope)
                height_q.appendleft((h, i))
            else:
                next_height.appendleft(height_q[0][1])
                height_q.appendleft((h, i))
        
        print(envelopes)
        print(next_length, next_height)
        for i in range(len_envelope):
            l, h = envelopes[i]

            next_l_ind = next_length[i]
            next_h_ind = next_height[i]

            print(i, next_l_ind, next_h_ind)

            if(next_l_ind == len_envelope or next_h_ind == len_envelope):
                continue
            
            final_ind = max(next_l_ind, next_h_ind)
            if(track[i] + 1 > track[final_ind]):
                track[final_ind] = track[i] + 1
            print(track)
        
        ans = max(track.values())
        return ans
        """

        #i tried monotonic stack, but it was not the correct approach.
        #it is basically the 2D longest subsequence problem

        #sorting as: (i) ascending the width/length of envelopes, (ii) descending the height of same width/length envelopes
        #note: i) thus, a new length/width of envelopes can increase the length of LIS only once, ii) placing the heights at the most optimal position opens the doors for the following envelopes to enlarge the sub-sequence.
        #note: LIS is not indicating the sub-sequnce, rather it just conveys the length of longest sub-sequence

        envelopes.sort(key = lambda x: [x[0], -x[1]])
        LIS = []
        for l, h in envelopes:
            ind = bisect_left(LIS, h)
            if(ind == len(LIS)):
                LIS.append(h)
            else:
                LIS[ind] = h
        return len(LIS)
