import heapq as hq
class StockPrice:

    def __init__(self):
        self.timestamps = {}
        self.latest_price = 0
        self.latest_time = 0
        self.max_heap = []
        self.min_heap = []
        self.stale = set()


    def update(self, timestamp: int, price: int) -> None:
        #check latest
        if(timestamp >= self.latest_time):
            self.latest_price = price
            self.latest_time = timestamp

        if(timestamp in self.timestamps):
            if(self.timestamps[timestamp] != price): #i missed this case where the upade on same timestampt with the same price == no update required
                self.stale.add((timestamp, self.timestamps[timestamp]))
                if((timestamp, price) in self.stale): #i missed this case where the previously seen price is again re-assigned == stale still holds the value
                    self.stale.remove((timestamp, price))
            else:
                return
        
        #keep in the map
        self.timestamps[timestamp] = price

        #keep in the heaps
        hq.heappush(self.max_heap, (-price, timestamp)) #i used [] instead of () while calling function
        hq.heappush(self.min_heap, (price, timestamp)) 
        return
        
    def current(self) -> int:
        return self.latest_price

    def maximum(self) -> int:
        h = self.max_heap
        while(h):
            price, time = h[0]
            price = -price
            if((time, price) in self.stale):
                hq.heappop(h)
            else:
                return price
        return -1

    def minimum(self) -> int:
        h = self.min_heap
        while(h):
            price, time = h[0]
            if((time, price) in self.stale):
                hq.heappop(h)
            else:
                return price
        return -1


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()