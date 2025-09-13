import heapq as hq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minh = []
        self.k = k

        for e in nums:
            hq.heappush(self.minh, e)
        
        while(len(self.minh)>k):
            hq.heappop(self.minh)

    def add(self, val: int) -> int:
        if(len(self.minh)==self.k):
            if(val<self.minh[0]):
                return self.minh[0]
            else:
                hq.heappush(self.minh, val)
                hq.heappop(self.minh)
                return self.minh[0]
        else:
            hq.heappush(self.minh, val)
            return self.minh[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

#0
#1 | 2
#3, 4 | 5, 6

