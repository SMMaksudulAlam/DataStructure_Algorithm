class RandomizedSet:

    def __init__(self):
        self.dic = {}
        self.lst = []

    def insert(self, val: int) -> bool:
        if(val in self.dic):
            return False
        self.dic[val] = len(self.lst)
        self.lst.append(val)
        return True

    def remove(self, val: int) -> bool:
        if(val not in self.dic):
            return False
        
        val_ind = self.dic[val]

        last_elem = self.lst[-1]
        last_ind = self.dic[last_elem]
        
        self.lst[val_ind], self.lst[last_ind] = self.lst[last_ind], self.lst[val_ind]

        self.dic[last_elem] = val_ind
        del self.dic[val]
        self.lst.pop()

        return True

    def getRandom(self) -> int:
        elem = random.choice(self.lst)
        return elem

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()