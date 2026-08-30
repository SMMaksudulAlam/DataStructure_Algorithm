class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        curr = 0
        if(not intervals):
            return [newInterval]
        if(newInterval[0]<intervals[curr][0]):
            ans.append(newInterval)
            newInterval = None
        else:
            ans.append(intervals[curr])
            curr+=1

        while(newInterval and curr<len(intervals)):
            if(newInterval[0]<intervals[curr][0]):
                if(ans[-1][1]>=newInterval[0]):
                    ans[-1][1] = max(ans[-1][1], newInterval[1])
                else:
                    ans.append(newInterval)
                newInterval = None
            else:
                ans.append(intervals[curr])
                curr += 1
        
        while(curr<len(intervals)):
            if(ans[-1][1]>=intervals[curr][0]):
                ans[-1][1] = max(ans[-1][1], intervals[curr][1])
            else:
                ans.append(intervals[curr])
            curr+=1
        
        if(newInterval):
            if(ans[-1][1]>=newInterval[0]):
                ans[-1][1] = max(ans[-1][1], newInterval[1])
            else:
                ans.append(newInterval)

        return ans
        

        
