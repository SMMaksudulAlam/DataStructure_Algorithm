import heapq as hq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:x[0])
        end_times = []
        count = 0
        for meeting in intervals:
            start_time = meeting[0]
            end_time = meeting[1]
            if(not end_times):
                count += 1
                hq.heappush(end_times, end_time)
            else:
                next_end_time = end_times[0]
                if(next_end_time<=start_time):
                    hq.heappop(end_times)
                else:
                    count+=1
                hq.heappush(end_times, end_time)
        return count

