import heapq as hq
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:

        meetings.sort(key = lambda x: x[0])

        ongoing_meetings = []
        available_meeting_rooms = []
        count = {}

        for i in range(n):
            hq.heappush(available_meeting_rooms, i)
            count[i] = 0
        
        
        for start, end in meetings:
            while(ongoing_meetings and ongoing_meetings[0][0]<=start):
                end_, id = hq.heappop(ongoing_meetings)
                hq.heappush(available_meeting_rooms, id)
                
            if(available_meeting_rooms):
                id = hq.heappop(available_meeting_rooms)
                count[id] += 1
                hq.heappush(ongoing_meetings, (end, id))
            else:
                end_, id = hq.heappop(ongoing_meetings)
                end = end_ + (end-start)
                count[id] += 1
                hq.heappush(ongoing_meetings, (end, id))
        
        maxi_count = max(count.values())
        
        for k, v in count.items():
            if(v==maxi_count):
                return k

        return -1

