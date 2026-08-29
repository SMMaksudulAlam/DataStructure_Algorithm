import heapq as hq
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meeting_rooms = []
        counter = {}
        for i in range(n):
            hq.heappush(meeting_rooms, (0, i))
            counter[i] = 0
        
        meetings.sort(key = lambda x: x[0])

        for meeting in meetings:
            start_time = meeting[0]
            end_time = meeting[1]

            if(meeting_rooms[0][0]<=start_time):
                available = []
                while(meeting_rooms and meeting_rooms[0][0]<=start_time):
                    element = hq.heappop(meeting_rooms)
                    element = (element[1], element[0])
                    hq.heappush(available, element)

                room_no, next_end_time = hq.heappop(available)
                counter[room_no] += 1
                hq.heappush(meeting_rooms, (end_time, room_no))

                while(available):
                    element = hq.heappop(available)
                    element = (element[1], element[0])
                    hq.heappush(meeting_rooms, element)

            else:
                next_end_time, room_no = hq.heappop(meeting_rooms)
                counter[room_no] += 1
                hq.heappush(meeting_rooms, (next_end_time + (end_time - start_time), room_no))

        ans = 0
        max_count = 0
        #print(meetings)
        #print(counter)
        for key, val in counter.items():
            if(max_count<val):
                max_count = val
                ans = key
        return ans
