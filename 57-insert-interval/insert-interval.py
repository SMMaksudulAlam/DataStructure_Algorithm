class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if(not intervals):
            return [newInterval]
        
        intervals.sort(key = lambda x:x[0])
        intervals = deque(intervals)
        ans = []
        while(intervals and newInterval):
            if(intervals[0][0]<newInterval[0]):
                ans.append(intervals.popleft())
            else:
                if(ans and ans[-1][1]>=newInterval[0]):
                    ans[-1][1] = max(ans[-1][1], newInterval[1])
                else:
                    ans.append(newInterval)
                newInterval = None

        while(intervals):
            if(ans[-1][1]>=intervals[0][0]):
                ans[-1][1] = max(ans[-1][1], intervals[0][1])
                intervals.popleft()
            else:
                ans.append(intervals.popleft())
        if(newInterval):
            if(ans[-1][1]>=newInterval[0]):
                    ans[-1][1] = max(ans[-1][1], newInterval[1])
            else:
                ans.append(newInterval)

        return ans