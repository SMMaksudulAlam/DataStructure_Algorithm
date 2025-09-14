import heapq as hq
class MedianFinder:

    def __init__(self):
        self.min = []
        self.max = []
       
    def balance(self):
        ln = len(self.min) + len(self.max)
        if(ln%2==0):
            if(len(self.min)<len(self.max)):
                while(len(self.min)<len(self.max)):
                    n = -hq.heappop(self.max)
                    hq.heappush(self.min, n)
            else:
                while(len(self.min)>len(self.max)):
                    n = hq.heappop(self.min)
                    hq.heappush(self.max, -n)
        else:
            if(len(self.min)<=len(self.max)):
                while(len(self.min)<=len(self.max)):
                    n = -hq.heappop(self.max)
                    hq.heappush(self.min, n)
            else:
                while(len(self.min)>len(self.max)+1):
                    n = hq.heappop(self.min)
                    hq.heappush(self.max, -n)

    def addNum(self, num: int) -> None:
        if(not self.min or num>=self.min[0]):
            hq.heappush(self.min, num)
            self.balance()
        else:
            hq.heappush(self.max, -num)
            self.balance()

    def findMedian(self) -> float:
        ln = len(self.min) + len(self.max)
        if(ln%2==0):
            return (self.min[0]-self.max[0])/2
        else:
            return self.min[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()