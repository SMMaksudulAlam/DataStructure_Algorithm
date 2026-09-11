class node:
    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.dic = {}
        self.head = node(-1, -1)
        self.tail = node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.count = 0

    def get(self, key: int) -> int:
        if(key not in self.dic):
            return -1

        nde = self.dic[key]
        nde.prev.next = nde.next
        nde.next.prev = nde.prev

        self.tail.prev.next = nde
        nde.prev = self.tail.prev

        nde.next = self.tail
        self.tail.prev = nde
        return nde.val


    def put(self, key: int, value: int) -> None:
        if(key in self.dic):
            self.get(key)
            self.dic[key] = self.tail.prev
            self.dic[key].val = value
            return
        
        nde = node(key, value)
        self.tail.prev.next = nde
        nde.prev = self.tail.prev
        nde.next = self.tail
        self.tail.prev = nde
        self.dic[key] = nde
        self.count += 1

        if(self.count > self.capacity):
            nde = self.head.next
            key = nde.key
            del self.dic[key]
            self.head.next = nde.next
            nde.next.prev = self.head
            self.count-=1
        return
        

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)