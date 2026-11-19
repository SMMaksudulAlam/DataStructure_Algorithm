"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        invs = []
        for emp_inv in schedule:
            invs += emp_inv
            
        invs.sort(key = lambda x:x.start)
        ans = []
        limit = invs[0].end
        for i in range(1, len(invs)):
            if(limit<invs[i].start):
                ans.append(Interval(limit, invs[i].start))
            limit = max(limit, invs[i].end)
        return ans