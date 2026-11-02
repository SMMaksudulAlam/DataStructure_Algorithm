class RLEIterator:

    def __init__(self, encoding: list[int]):
        self.q = deque()
        i = 0
        while(i<len(encoding)):
            count = encoding[i]
            num = encoding[i+1]
            if(count > 0):
                self.q.append(count)
                self.q.append(num)
            i+=2
        return

    def next(self, n: int) -> int:
        count = 0
        if(not self.q):
            return -1
        cnt = 0
        val = -1
        while(self.q and count+self.q[0]<=n):
            cnt = self.q.popleft()
            val = self.q.popleft()
            count += cnt
        if(count == n):
            return val
        if(not self.q):
            return -1
        
        self.q[0] = count + self.q[0] - n
        return self.q[1]
        

# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)